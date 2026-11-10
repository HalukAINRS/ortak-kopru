# durum_satiri.ps1 - Claude Code durum satiri: ortam nerede, hangi uzak yerler ekli.
#
# Girdi : Claude Code'un stdin'e verdigi JSON (workspace.project_dir, workspace.current_dir,
#         workspace.added_dirs, session_name, version).
# Cikti : tek satir. Ornek:  karargah | uzak: C:\proje (+1) | ad: proje | 2.1.322
#
#   karargah              oturum kapidan acildi ve karargah kokunde
#   ORTAM KAYDI: <yol>    oturum kapidan acildi ama kok baska yere tasinmis (/cd, worktree)
#   KAPI DISI: <yol>      oturum kapidan acilmamis (KARARGAH_ROOT ortamda yok)
#   konum: <yol>          kabuk su an kokten baska bir klasorde (ortam degismedi)
#   uzak: <yol> (+N)      eklenen uzak yerler; yoksa "uzak: yok"
#   ad: <ad>              oturum adi (-n, /rename)
#
# Dosya ASCII'dir; Windows PowerShell 5.1 ve PowerShell 7 ile calisir. Girdi ve cikti UTF-8 bayt
# olarak okunur ve yazilir; konsolun kod sayfasina bagli degildir.

$ErrorActionPreference = 'Stop'
$utf8 = New-Object System.Text.UTF8Encoding($false)

function Duz([string]$yol) {
    # Karsilastirma ve gosterim icin: egik cizgi ters boluye cevrilir, sondaki ayrac atilir.
    if (-not $yol) { return '' }
    $y = $yol.Replace('/', '\').TrimEnd('\')
    if ($y.EndsWith(':')) { $y = $y + '\' }
    return $y
}

function Ayni([string]$a, [string]$b) {
    return [string]::Equals($a, $b, [System.StringComparison]::OrdinalIgnoreCase)
}

try {
    $giris = [Console]::OpenStandardInput()
    $bellek = New-Object System.IO.MemoryStream
    $giris.CopyTo($bellek)
    $veri = $utf8.GetString($bellek.ToArray()) | ConvertFrom-Json

    $kok = Duz $env:KARARGAH_ROOT
    $proje = ''
    $konum = ''
    $ekli = @()
    if ($veri.workspace) {
        $proje = Duz ([string]$veri.workspace.project_dir)
        $konum = Duz ([string]$veri.workspace.current_dir)
        if ($veri.workspace.added_dirs) { $ekli = @($veri.workspace.added_dirs) }
    }
    if (-not $konum) { $konum = Duz ([string]$veri.cwd) }
    if (-not $proje) { $proje = $konum }

    $parca = New-Object 'System.Collections.Generic.List[string]'
    if (-not $proje) {
        $parca.Add('ortam bilinmiyor')
    } elseif (-not $kok) {
        $parca.Add('KAPI DISI: ' + $proje)
    } elseif (Ayni $proje $kok) {
        $parca.Add('karargah')
    } else {
        $parca.Add('ORTAM KAYDI: ' + $proje)
    }
    if ($konum -and -not (Ayni $konum $proje)) { $parca.Add('konum: ' + $konum) }

    if ($ekli.Count -gt 0) {
        $ilk = Duz ([string]$ekli[0])
        if ($ekli.Count -gt 1) { $ilk = $ilk + ' (+' + ($ekli.Count - 1) + ')' }
        $parca.Add('uzak: ' + $ilk)
    } else {
        $parca.Add('uzak: yok')
    }

    if ($veri.session_name) { $parca.Add('ad: ' + [string]$veri.session_name) }
    if ($veri.version) { $parca.Add([string]$veri.version) }
    $satir = [string]::Join(' | ', $parca.ToArray())
} catch {
    $satir = 'durum satiri okunamadi: ' + $_.Exception.Message
}

$bayt = $utf8.GetBytes($satir)
$cikis = [Console]::OpenStandardOutput()
$cikis.Write($bayt, 0, $bayt.Length)
$cikis.Flush()
