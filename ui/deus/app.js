"use strict";

const $ = (id) => document.getElementById(id);

// The per-launch token arrives only in the local launch URL fragment. It is
// never served in HTML or sent as part of an HTTP URL.
const incomingToken = new URLSearchParams(location.hash.slice(1)).get("token");
if (incomingToken) {
  sessionStorage.setItem("deus-session-token", incomingToken);
  history.replaceState(null, "", location.pathname);
}
const token = sessionStorage.getItem("deus-session-token") || "";
const statuses = {
  ready: "Hazır",
  running: "Çalışılıyor",
  paused: "Duraklatıldı",
  awaiting_verification: "Doğrulama bekliyor",
  blocked: "Engelde",
  completed: "Tamamlandı",
  cancelled: "Durduruldu",
};

let tasks = [];
let current = null;
let context = null;
let activeView = "work";
let runtimeReady = false;
let selection = 0;
let busy = false;
let receiveDraft = null;
let resultDraft = null;
let verificationDraft = null;
const pendingRequests = new Map();

const key = () => crypto.randomUUID();
const lines = (value) => value.split(/\r?\n/).map((line) => line.trim()).filter(Boolean);
const isClosed = () => ["completed", "cancelled"].includes(current?.status);
const activeAttempt = () => current?.attempts.find((attempt) => attempt.id === current.active_attempt_id);
const currentResult = () => current?.results.find((result) => result.id === current.current_result_id);

function node(tag, text, className) {
  const element = document.createElement(tag);
  if (text !== undefined) element.textContent = text;
  if (className) element.className = className;
  return element;
}

function notice(message, error = false) {
  $("notice").textContent = message;
  $("notice").className = error ? "notice error" : "notice";
  $("notice").setAttribute("role", error ? "alert" : "status");
  $("notice").hidden = !message;
}

function formError(id, message = "") {
  if (!id) return;
  $(id).textContent = message;
  $(id).hidden = !message;
}

async function api(path, data) {
  const options = {headers: {"X-Deus-Token": token}, cache: "no-store"};
  if (data !== undefined) {
    options.method = "POST";
    options.headers["Content-Type"] = "application/json";
    options.body = JSON.stringify(data);
  }
  const response = await fetch(path, options);
  const body = await response.json();
  if (!response.ok) {
    const message = typeof body.error === "string" ? body.error :
      body.error?.message || body.message || `İşlem tamamlanmadı (${response.status}).`;
    const error = new Error(message);
    error.status = response.status;
    throw error;
  }
  return body;
}

// Keep the same key after an uncertain response, provided the exact payload
// is unchanged. A retry must not turn one declaration into a second event.
async function post(path, data) {
  const signature = JSON.stringify(data);
  let pending = pendingRequests.get(path);
  if (!pending || pending.signature !== signature) {
    pending = {signature, key: key()};
    pendingRequests.set(path, pending);
  }
  const response = await api(path, {...data, request_key: pending.key});
  pendingRequests.delete(path);
  return response;
}

function taskWords(task) {
  return task.current_words || task.original_words || "";
}

function title(task) {
  const firstLine = taskWords(task).split("\n")[0];
  return firstLine.length > 110 ? `${firstLine.slice(0, 107)}…` : firstLine;
}

function renderList() {
  const query = $("search").value.toLocaleLowerCase("tr");
  const list = $("task-list");
  list.replaceChildren();
  const visible = tasks.filter((task) =>
    `${taskWords(task)} ${task.id}`.toLocaleLowerCase("tr").includes(query));
  const open = tasks.filter((task) => !["completed", "cancelled"].includes(task.status));
  $("task-count").textContent = `${tasks.length} iş · ${open.length} açık`;
  for (const task of visible) {
    const button = node("button", undefined, `task-item${current?.id === task.id ? " active" : ""}`);
    button.type = "button";
    button.append(node("span", title(task)), node("small", statuses[task.status] || task.status));
    button.onclick = () => selectTask(task.id).catch((error) => notice(error.message, true));
    list.append(button);
  }
  if (!visible.length) {
    list.append(node("p", tasks.length ? "Aramaya uyan iş yok." : "Henüz iş yok.", "muted"));
  }
}

function appendFiles(container, files, emptyMessage) {
  for (const file of files) {
    const row = node("div", undefined, "source-item");
    row.append(node("strong", file.name || file.original_path || file.path || file.id));
    if (file.note) row.append(node("p", file.note, "muted"));
    const details = node("details");
    details.append(node("summary", "Saklanan dosyanın bilgisi"));
    details.append(node("p", `${file.bytes ?? "?"} bayt · SHA-256: ${file.sha256 || "Belirtilmedi"}`, "binding"));
    row.append(details);
    container.append(row);
  }
  if (!files.length) container.append(node("p", emptyMessage, "muted"));
}

function renderProgress() {
  const progress = $("progress");
  progress.replaceChildren();
  const attempt = activeAttempt();
  if (attempt) progress.append(node("p", `${attempt.participant} · ${attempt.session_id}`));
  const result = currentResult() || current.results.at(-1);
  if (!result) {
    progress.append(node("p", attempt ?
      "Atama kayıtlı. Alım beyanı ve somut sonuç bekleniyor." :
      "İş hazır. Bir oturuma atanabilir; kaynak paketi devir görünümünde bulunur.", "muted"));
    return;
  }
  progress.append(node("p", result.summary, "prose"));
  if (result.id !== current.current_result_id) {
    progress.append(node("p", "Bu sonuç önceki çalıştırmaya aittir; güncel işi kapatmaz.", "muted"));
  }
  const artifacts = node("div", undefined, "result-artifacts");
  artifacts.append(node("h4", "Teslim edilen dosyalar"));
  appendFiles(artifacts, result.artifacts || [], "Bu sonuç için dosya teslim edilmedi.");
  progress.append(artifacts);
  if (result.id !== current.current_result_id) return;
  const checks = current.verification || [];
  if (!checks.length) {
    progress.append(node("p", "Sonuç teslim edildi. Ölçütler henüz doğrulanmadı.", "muted"));
    return;
  }
  const receipts = node("div", undefined, "verification-receipts");
  receipts.id = "recorded-checks";
  receipts.append(node("h4", "Kaydedilmiş denetimler"));
  for (const check of checks) {
    const criterion = current.criteria.find((item) => item.id === check.criterion_id);
    const row = node("article", undefined, "check-receipt");
    row.append(node("strong", criterion?.description || check.criterion_id));
    row.append(node("p", `${check.passed ? "Geçer" : "Kalır"} · Denetleyen: ${check.verifier}`,
      check.passed ? "check-pass" : "check-fail"));
    row.append(node("p", check.evidence, "prose"));
    receipts.append(row);
  }
  progress.append(receipts);
}

function matchesAttempt(draft) {
  return Boolean(draft && current && draft.taskId === current.id &&
    draft.revision === current.revision && draft.attemptId === current.active_attempt_id);
}

function matchesResult(draft) {
  return Boolean(draft && current && draft.taskId === current.id &&
    draft.revision === current.revision && draft.resultId === current.current_result_id);
}

function prepareResultDraft() {
  const attempt = activeAttempt();
  resultDraft = attempt ? {
    taskId: current.id, revision: current.revision,
    attemptId: attempt.id, sessionId: attempt.session_id,
  } : null;
  $("result-form").reset();
  formError("result-error");
  if (attempt?.status === "received") $("result-card").open = true;
}

function addLabel(container, caption, control) {
  const label = node("label", caption);
  label.htmlFor = control.id;
  label.append(control);
  container.append(label);
}

function prepareVerificationDraft() {
  const result = currentResult();
  const attempt = current.attempts.find((item) => item.id === result?.attempt_id);
  verificationDraft = result ? {
    taskId: current.id, revision: current.revision, resultId: result.id,
    sessionId: attempt?.session_id || "Belirtilmedi", summary: result.summary,
    criteria: current.criteria.map((criterion) => ({...criterion})),
  } : null;
  const fields = $("verification-fields");
  fields.replaceChildren();
  formError("verify-error");
  if (!verificationDraft) return;
  verificationDraft.criteria.forEach((criterion, index) => {
    const group = node("fieldset", undefined, "criterion-check");
    group.append(node("legend", `${index + 1}. ${criterion.description}`));
    const verdict = node("select");
    verdict.id = `check-${index}-status`;
    verdict.required = true;
    for (const [value, label] of [["", "Karar seç"], ["true", "Geçer"], ["false", "Kalır"]]) {
      const option = node("option", label);
      option.value = value;
      verdict.append(option);
    }
    addLabel(group, "Bu ölçüt karşılandı mı?", verdict);
    const evidence = node("textarea");
    evidence.id = `check-${index}-evidence`;
    evidence.rows = 3;
    evidence.required = true;
    evidence.placeholder = "Gözlemini, kontrol sonucunu veya dosya içindeki dayanağı belirt.";
    addLabel(group, "Kanıt ve gözlem", evidence);
    const verifier = node("input");
    verifier.id = `check-${index}-verifier`;
    verifier.required = true;
    verifier.autocomplete = "off";
    verifier.placeholder = "Denetimi yapan kişi veya oturum";
    addLabel(group, "Denetleyen", verifier);
    fields.append(group);
  });
  if (["awaiting_verification", "blocked"].includes(current.status)) $("verify-card").open = true;
}

function resetWorkflowDrafts() {
  receiveDraft = null;
  resultDraft = null;
  verificationDraft = null;
  $("receive-form").reset();
  $("result-form").reset();
  $("verification-fields").replaceChildren();
  for (const id of ["receive-error", "result-error", "verify-error"]) formError(id);
  $("result-card").open = false;
  $("verify-card").open = false;
}

function renderWorkflow() {
  const attempt = activeAttempt();
  const receiptAvailable = attempt?.status === "assigned" && current.status === "ready";
  if (!matchesAttempt(receiveDraft)) {
    receiveDraft = attempt ? {
      taskId: current.id, revision: current.revision,
      attemptId: attempt.id, sessionId: attempt.session_id,
    } : null;
    $("receive-confirm").checked = false;
  }
  $("receive-form").hidden = !receiptAvailable;
  $("receive-target").textContent = attempt ? `Sürüm ${current.revision} · Oturum: ${attempt.session_id}` : "";
  $("receive-binding").textContent = attempt ? `Çalıştırma: ${attempt.id}` : "";
  $("receive-state").textContent = !attempt ? "Önce bu işi bir oturuma ata." :
    attempt.status === "received" ? "Bu oturumun alım beyanı kayıtlı. Sonuç teslim edilebilir." :
    attempt.status === "result_submitted" ? "Alım beyanı ve bu çalıştırmanın sonucu kayıtlı." :
    "Atanmış oturumun işi alması için açık beyan gerekiyor.";

  // A draft belongs to the attempt/result visible when it was opened. Refresh
  // must never silently attach the user's old evidence to a newer result.
  if (!resultDraft && attempt && ["assigned", "received"].includes(attempt.status)) prepareResultDraft();
  const staleAttempt = resultDraft && !matchesAttempt(resultDraft);
  $("result-target").textContent = resultDraft ?
    `Bu taslak: sürüm ${resultDraft.revision} · Oturum: ${resultDraft.sessionId}` : "";
  $("result-binding").textContent = resultDraft ? `Çalıştırma: ${resultDraft.attemptId}` :
    attempt ? `Çalıştırma: ${attempt.id}` : "Henüz bir atama yok.";
  $("result-stale").hidden = !staleAttempt;
  $("result-stale").textContent = staleAttempt ?
    "Atama veya istek sürümü değişti. Bu taslak önceki çalıştırmaya bağlıdır; güncel atama için yeni taslak açman gerekir. Yeni taslak açılırken aşağıdaki alanlar temizlenir." : "";
  $("load-current-attempt").hidden = !(staleAttempt && attempt && ["assigned", "received"].includes(attempt.status));
  $("result-guide").textContent = isClosed() ? "İş kapalı; yeni sonuç teslim edilemez." :
    attempt?.status === "received" ? "Alım beyanı verilen oturumun somut sonucunu kaydet." :
    attempt?.status === "result_submitted" ? "Bu çalıştırmanın sonucu teslim edildi. Yeni bir sonuç için yeni atama gerekir." :
    "Sonuç tesliminden önce güncel atama ve alım beyanı gerekir.";
  $("result-form").hidden = !resultDraft || isClosed();

  if (!verificationDraft && currentResult()) prepareVerificationDraft();
  const staleResult = verificationDraft && !matchesResult(verificationDraft);
  $("verify-target").textContent = verificationDraft ?
    `Bu denetim: sürüm ${verificationDraft.revision} · Oturum: ${verificationDraft.sessionId}` : "";
  $("verify-binding").textContent = verificationDraft ?
    `Sonuç: ${verificationDraft.resultId}\nTeslim özeti: ${verificationDraft.summary}` : "Henüz denetlenecek sonuç yok.";
  $("verify-stale").hidden = !staleResult;
  $("verify-stale").textContent = staleResult ?
    "Güncel sonuç veya istek sürümü değişti. Bu denetim önceki sonuca bağlıdır ve gönderilemez. Yeni denetim açılırken karar, kanıt ve denetleyen alanları temizlenir." : "";
  $("load-current-result").hidden = !(staleResult && currentResult());
  $("verify-guide").textContent = current.status === "completed" ?
    "Tüm ölçütlerin geçer beyanı kaydedildi; iş tamamlandı. Kaydedilmiş denetimler yukarıda yer alıyor." :
    current.status === "blocked" ?
    "En az bir ölçüt kalır olarak kaydedildi. Yeniden denetleyeceksen her ölçüt için yeni kararını ve kanıtını açıkça gir." :
    current.status === "awaiting_verification" ?
    "Teslim edilen sonucu ölçütlerle karşılaştır. Hiçbir karar kendiliğinden seçilmez." :
    "Güncel bir sonuç teslim edildiğinde ölçütlere bağlı denetim açılır.";
  $("verify-form").hidden = !verificationDraft || isClosed();
  renderAvailability();
}

function disableForm(id, disabled) {
  for (const field of $(id).elements) field.disabled = disabled;
}

function renderAvailability() {
  $("new-task").disabled = busy || !runtimeReady;
  if (!current) return;
  const attempt = activeAttempt();
  const mutable = !busy && runtimeReady && !isClosed();
  $("pause-task").disabled = busy || !["ready", "running", "awaiting_verification", "blocked"].includes(current.status);
  $("resume-task").disabled = !mutable || current.status !== "paused";
  $("cancel-task").disabled = busy || isClosed();
  disableForm("revise-form", !mutable);
  disableForm("assign-form", !mutable || current.status === "paused");
  disableForm("receive-form", !mutable || !matchesAttempt(receiveDraft) || attempt?.status !== "assigned");
  disableForm("result-form", !mutable || !matchesAttempt(resultDraft) || attempt?.status !== "received" || current.status !== "running");
  disableForm("verify-form", !mutable || !matchesResult(verificationDraft) || !["awaiting_verification", "blocked"].includes(current.status));
  $("load-current-attempt").disabled = !mutable;
  $("load-current-result").disabled = !mutable;
}

function renderTask() {
  $("empty").hidden = true;
  $("task-detail").hidden = false;
  $("task-id").textContent = current.id;
  $("task-title").textContent = title(current);
  $("task-status").textContent = statuses[current.status] || current.status;
  $("current-words").textContent = taskWords(current);
  $("original-words").textContent = current.original_words;
  $("revision-note").textContent = `Sürüm ${current.revision} · Özgün söz ve önceki sürümler geçmişte korunur.`;
  $("criteria").replaceChildren(...current.criteria.map((criterion) => node("li", criterion.description)));
  $("revised-words").value = taskWords(current);
  const authority = $("authority");
  authority.replaceChildren();
  for (const [label, value] of [["Söyleyen", current.authority.actor],
    ["Kaynak", current.authority.source], ["Kapsam", current.authority.scope]]) {
    authority.append(node("dt", label), node("dd", value || "Belirtilmedi"));
  }
  $("sources").replaceChildren();
  appendFiles($("sources"), current.sources, "Bu işe dosya kaynağı eklenmedi.");
  renderProgress();
  renderWorkflow();
  showView(activeView);
  renderList();
}

function showView(view) {
  activeView = view;
  for (const name of ["work", "sources", "history"]) $(`${name}-view`).hidden = name !== view;
  document.querySelectorAll("[data-view]").forEach((button) =>
    button.setAttribute("aria-pressed", String(button.dataset.view === view)));
}

async function selectTask(id) {
  const selected = ++selection;
  const base = `/api/tasks/${encodeURIComponent(id)}`;
  const [task, bundle, history] = await Promise.all([api(base), api(`${base}/context`), api(`${base}/events`)]);
  if (selected !== selection) return;
  if (current?.id !== task.id) resetWorkflowDrafts();
  current = task;
  context = bundle;
  $("context").textContent = JSON.stringify(bundle, null, 2);
  $("events").replaceChildren(...history.events.map((event) => {
    const item = node("li");
    item.append(node("strong", event.kind || "Olay"), node("time", event.at || event.created_at || ""));
    if (event.data) {
      const details = node("details");
      details.append(node("summary", "Ayrıntı"), node("pre", JSON.stringify(event.data, null, 2)));
      item.append(details);
    }
    return item;
  }));
  renderTask();
}

async function refresh() {
  const [data, runtime] = await Promise.all([api("/api/tasks"), api("/api/runtime")]);
  runtimeReady = runtime.ready === true;
  $("runtime").textContent = runtime.kernel_verified === true ?
    "NT çekirdek uç noktası doğrulandı · İş yürütümü kullanıcı kipinde" :
    runtime.backend === "portable" ? "Taşınabilir geliştirme kipi · NT çekirdek bağlantısı yok" :
    "NT çekirdek bağlantısı doğrulanmadı · Yeni çalışma engellendi";
  tasks = data.tasks;
  renderList();
  if (current) await selectTask(current.id);
  renderAvailability();
}

async function mutate(path, data, message, errorId, onSuccess) {
  if (busy) return;
  busy = true;
  formError(errorId);
  renderAvailability();
  try {
    const response = await post(path, data);
    if (onSuccess) onSuccess(response);
    try {
      await refresh();
      notice(message);
    } catch (error) {
      notice(`${message} Görünüm yenilenemedi; Durumu yenile ile tekrar yükle. ${error.message}`, true);
    }
  } catch (error) {
    if (error.status === 409 || error.status === 503) {
      try { await refresh(); } catch (_) { /* Keep the submitted draft on failure. */ }
    }
    formError(errorId, error.message);
    notice(error.message, true);
  } finally {
    busy = false;
    renderAvailability();
  }
}

async function update(action, data) {
  if (!current) return;
  await mutate(`/api/tasks/${encodeURIComponent(current.id)}/${action}`,
    {...data, expected_revision: current.revision}, "İş kaydı güncellendi.");
}

for (const button of document.querySelectorAll("[data-view]")) {
  button.onclick = () => showView(button.dataset.view);
}
$("search").oninput = renderList;
$("refresh").onclick = () => refresh().catch((error) => notice(error.message, true));
$("new-task").onclick = () => {
  formError("create-error");
  $("create-dialog").showModal();
};
$("close-dialog").onclick = () => $("create-dialog").close();

$("create-form").onsubmit = async (event) => {
  event.preventDefault();
  if (busy) return;
  const button = event.submitter;
  button.disabled = true;
  const payload = {
    original_words: $("new-words").value,
    authority: {actor: "Haluk", source: "deus_ex_machina yerel kullanıcı girdisi", scope: $("new-scope").value},
    criteria: lines($("new-criteria").value),
    sources: lines($("new-sources").value),
  };
  await mutate("/api/tasks", payload, "İş oluşturuldu. Özgün söz ve kapsam kaydedildi.", "create-error", (task) => {
    $("create-dialog").close();
    $("create-form").reset();
    resetWorkflowDrafts();
    current = task;
  });
  button.disabled = false;
};

$("revise-form").onsubmit = (event) => {
  event.preventDefault();
  update("revise", {original_words: $("revised-words").value});
};
$("assign-form").onsubmit = (event) => {
  event.preventDefault();
  update("assign", {
    participant: $("participant").value,
    session_id: $("session").value,
    expected_active_attempt_id: current?.active_attempt_id || null,
  });
};
for (const [id, action] of [["pause-task", "pause"], ["resume-task", "resume"], ["cancel-task", "cancel"]]) {
  $(id).onclick = () => update("control", {action});
}

$("receive-form").onsubmit = (event) => {
  event.preventDefault();
  if (!matchesAttempt(receiveDraft) || !$("receive-confirm").checked) return;
  const draft = {...receiveDraft};
  mutate(`/api/attempts/${encodeURIComponent(draft.attemptId)}/receive`,
    {session_id: draft.sessionId}, "Alım beyanı kaydedildi. Sonuç teslim edilebilir.", "receive-error", () => {
      $("receive-confirm").checked = false;
      if (current?.id === draft.taskId) $("result-card").open = true;
    });
};
$("load-current-attempt").onclick = () => {
  prepareResultDraft();
  renderWorkflow();
};
$("result-form").onsubmit = (event) => {
  event.preventDefault();
  if (!matchesAttempt(resultDraft)) return;
  const draft = {...resultDraft};
  const payload = {
    session_id: draft.sessionId,
    summary: $("result-summary").value,
    artifacts: lines($("result-artifacts").value),
  };
  mutate(`/api/attempts/${encodeURIComponent(draft.attemptId)}/result`, payload,
    "Sonuç teslim edildi. Ölçütlere göre doğrulama bekliyor.", "result-error", () => {
      if (current?.id === draft.taskId) {
        resultDraft = null;
        $("result-form").reset();
        $("result-card").open = false;
      }
    });
};
$("load-current-result").onclick = () => {
  prepareVerificationDraft();
  renderWorkflow();
};
$("verify-form").onsubmit = (event) => {
  event.preventDefault();
  if (!matchesResult(verificationDraft)) return;
  const draft = verificationDraft;
  const checks = draft.criteria.map((criterion, index) => ({
    criterion_id: criterion.id,
    result_id: draft.resultId,
    passed: $(`check-${index}-status`).value === "true",
    evidence: $(`check-${index}-evidence`).value,
    verifier: $(`check-${index}-verifier`).value,
  }));
  // Native required controls enforce an explicit choice. Also guard scripted
  // submission so an empty option can never be converted into a false receipt.
  if (draft.criteria.some((_, index) => !["true", "false"].includes($(`check-${index}-status`).value))) return;
  mutate(`/api/tasks/${encodeURIComponent(draft.taskId)}/verify`,
    {checks, expected_revision: draft.revision}, "Denetim beyanları kaydedildi.", "verify-error", () => {
      if (current?.id === draft.taskId) verificationDraft = null;
    });
};

$("download-context").onclick = () => {
  if (!context) return;
  const blob = new Blob([`${JSON.stringify(context, null, 2)}\n`], {type: "application/json"});
  const url = URL.createObjectURL(blob);
  const link = node("a");
  link.href = url;
  link.download = `deus-${current.id}-s${current.revision}.json`;
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
};

async function start() {
  if (!token) {
    $("runtime").textContent = "Yerel başlatma bağlantısı gerekli";
    $("new-task").disabled = true;
    notice("Sunucuyu başlattığın terminaldeki launch_url bağlantısını aç. Erişim anahtarı bu sayfadan alınamaz.");
    return;
  }
  try {
    await refresh();
  } catch (error) {
    $("runtime").textContent = "Çalışma ortamına bağlanılamadı";
    $("new-task").disabled = true;
    notice(error.message, true);
  }
}
start();
