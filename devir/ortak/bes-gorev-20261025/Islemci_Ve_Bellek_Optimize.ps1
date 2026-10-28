# HalukAI — İşlemci Kompleksi (i7-1255U P-Core / E-Core) ve Bellek (16 GB -> 32 GB Dual-Channel) Bakım/Optimizasyon Aracı
param(
    [ValidateSet("Durum", "Dengele", "Ram32Kontrol")]
    [string]$Mod = "Durum"
)

$ErrorActionPreference = "SilentlyContinue"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Alder Lake-U i7-1255U Topolojisi:
# P-Cores (2 Fiziksel / 4 Mantıksal HT): CPU 0, 1, 2, 3 -> Maske: 0x00F (15)
# E-Cores (8 Fiziksel / 8 Mantıksal):    CPU 4..11     -> Maske: 0xFF0 (4080)
# Hibrit Tam Maske (12 Mantıksal):       CPU 0..11     -> Maske: 0xFFF (4095)
# CPU 0 ve 1 ayni fiziksel P-Core un SMT kardesleridir; iki P-Core diye sayilmaz.
# Dengele: sabit P/E sabitlemesi yerine cevrimici mantiksal islemcileri Windows zamanlayicisina birakir.

function Get-DonanimDurumu {
    $os = Get-CimInstance Win32_OperatingSystem
    $cpu = Get-CimInstance Win32_Processor
    $dimms = @(Get-CimInstance Win32_PhysicalMemory)
    $xDrive = Get-PSDrive -Name X
    $yDrive = Get-PSDrive -Name Y

    $totalRamMB = [math]::Round($os.TotalVisibleMemorySize / 1024, 1)
    $freeRamMB = [math]::Round($os.FreePhysicalMemory / 1024, 1)
    $totalVirtMB = [math]::Round($os.TotalVirtualMemorySize / 1024, 1)
    $freeVirtMB = [math]::Round($os.FreeVirtualMemory / 1024, 1)
    $dualChannel = ($dimms.Count -ge 2)

    $procs = Get-Process | Where-Object { $_.WorkingSet64 -gt 25MB } | Sort-Object WorkingSet64 -Descending | ForEach-Object {
        [ordered]@{
            Name = $_.ProcessName
            Id = $_.Id
            WorkingSetMB = [math]::Round($_.WorkingSet64 / 1MB, 1)
            PrivateMB = [math]::Round($_.PrivateMemorySize64 / 1MB, 1)
            Threads = $_.Threads.Count
            Priority = [string]$_.PriorityClass
            AffinityHex = ("0x{0:X3}" -f [int64]$_.ProcessorAffinity)
        }
    }

    return [ordered]@{
        Timestamp = (Get-Date).ToString("o")
        Processor = [ordered]@{
            Name = $cpu.Name.Trim()
            Cores = $cpu.NumberOfCores
            LogicalProcessors = $cpu.NumberOfLogicalProcessors
            PCoreMask = "0x00F (CPU 0..3)"
            ECoreMask = "0xFF0 (CPU 4..11)"
            CurrentClockMHz = $cpu.CurrentClockSpeed
            MaxClockMHz = $cpu.MaxClockSpeed
            LoadPercentage = $cpu.LoadPercentage
        }
        Memory = [ordered]@{
            InstalledDIMMs = $dimms.Count
            ChannelMode = if ($dualChannel) { "Birden fazla DIMM raporlandi; kanal modu olculmedi" } else { "Tek DIMM raporlandi; bos yuva yeri ve kanal modu ayrica dogrulanir" }
            TotalVisibleMB = $totalRamMB
            FreePhysicalMB = $freeRamMB
            TotalCommitLimitMB = $totalVirtMB
            FreeCommitHeadroomMB = $freeVirtMB
            CommitPressureWarning = ($freeVirtMB -lt 3072)
        }
        Drives = [ordered]@{
            X_RAMDisk_UsedMB = [math]::Round($xDrive.Used / 1MB, 1)
            X_RAMDisk_FreeMB = [math]::Round($xDrive.Free / 1MB, 1)
            Y_USB_UsedGB = [math]::Round($yDrive.Used / 1GB, 2)
            Y_USB_FreeGB = [math]::Round($yDrive.Free / 1GB, 2)
        }
        TopProcesses = $procs
    }
}

if ($Mod -eq "Durum") {
    $durum = Get-DonanimDurumu
    $durum | ConvertTo-Json -Depth 5
    exit 0
}

if ($Mod -eq "Dengele") {
    $logicalCount = [int](Get-CimInstance Win32_Processor -ErrorAction Stop |
        Measure-Object -Property NumberOfLogicalProcessors -Sum).Sum
    if ($logicalCount -lt 1 -or $logicalCount -gt 63) {
        throw "Bu profil tek islemci grubu icin 1..63 mantiksal islemci bekler."
    }
    $fullMask = [int64]([math]::Pow(2, $logicalCount) - 1)
    $changes = @(Get-Process -Name "qemu-system-aarch64", "agy", "codex", "copilot" -ErrorAction SilentlyContinue | ForEach-Object {
        $item = $_
        try {
            $oldAff = [int64]$item.ProcessorAffinity
            $oldPriority = [string]$item.PriorityClass
            $item.ProcessorAffinity = [IntPtr]$fullMask
            if ($item.ProcessName -eq "qemu-system-aarch64") { $item.PriorityClass = "Normal" }
            $item.Refresh()
            if ([int64]$item.ProcessorAffinity -ne $fullMask) { throw "Affinity dogrulanamadi." }
            [ordered]@{ Process=$item.ProcessName; Id=$item.Id; Applied=$true
                OldAffinity=("0x{0:X}" -f $oldAff); NewAffinity=("0x{0:X}" -f [int64]$item.ProcessorAffinity)
                OldPriority=$oldPriority; Priority=[string]$item.PriorityClass }
        } catch {
            [ordered]@{ Process=$item.ProcessName; Id=$item.Id; Applied=$false; ErrorType=$_.Exception.GetType().Name }
        }
    })
    [ordered]@{ Status=if (@($changes | Where-Object { -not $_.Applied }).Count) { "Partial" } else { "Balanced" }
        Policy="WindowsScheduler_AllOnlineCPUs_QemuNormal"; AppliedChanges=$changes
        SuspendedProcessesResumed=$false; MemoryProfileChanged=$false; PostState=Get-DonanimDurumu
    } | ConvertTo-Json -Depth 6
    exit 0
}

if ($Mod -eq "Ram32Kontrol") {
    $dimms = @(Get-CimInstance Win32_PhysicalMemory)
    $totalGB = [math]::Round(($dimms | Measure-Object -Property Capacity -Sum).Sum / 1GB, 1)
    [ordered]@{
        InstalledDIMMCount = $dimms.Count
        TotalPhysicalGB = $totalGB
        DualChannelReady = ($dimms.Count -ge 2 -and $totalGB -ge 30)
        DualChannelMeasured = $false
        ProfileApplied = $false
        RecommendedQemuArgs = if ($totalGB -ge 30) {
            "-smp 6,sockets=1,cores=6,threads=1 -m 6144 -accel tcg,thread=multi,tb-size=2048"
        } else {
            "-smp 4,sockets=1,cores=4,threads=1 -m 3072 -accel tcg,thread=multi,tb-size=1024"
        }
        DIMMSlots = $dimms | ForEach-Object {
            [ordered]@{
                DeviceLocator = $_.DeviceLocator
                BankLabel = $_.BankLabel
                CapacityGB = [math]::Round($_.Capacity / 1GB, 1)
                SpeedMHz = $_.Speed
                ConfiguredClockMHz = $_.ConfiguredClockSpeed
                Manufacturer = $_.Manufacturer
                PartNumber = $_.PartNumber.Trim()
            }
        }
    } | ConvertTo-Json -Depth 5
    exit 0
}
