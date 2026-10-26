"use strict";
const $ = (id) => document.getElementById(id);
// The per-launch token arrives only in the local launch URL fragment. It is
// never served in HTML or sent as part of an HTTP URL.
const incomingToken = new URLSearchParams(location.hash.slice(1)).get('token');
if(incomingToken){sessionStorage.setItem('deus-session-token',incomingToken);history.replaceState(null,'',location.pathname);}
const token = sessionStorage.getItem('deus-session-token')||'';
const statuses = {ready:"Hazır",running:"Çalışılıyor",paused:"Duraklatıldı",awaiting_verification:"Doğrulama bekliyor",blocked:"Engelde",completed:"Tamamlandı",cancelled:"Durduruldu"};
let tasks = [], current = null, context = null, activeView = "work", pendingCreate = null, runtimeReady = false, selection = 0;
const key = () => crypto.randomUUID();
const lines = (value) => value.split(/\r?\n/).map(x=>x.trim()).filter(Boolean);
function node(tag, text, className) {const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(className)n.className=className;return n;}
function notice(message, error=false) {$('notice').textContent=message;$('notice').className=error?'notice error':'notice';$('notice').hidden=!message;}
async function api(path, data) {
  const options={headers:{'X-Deus-Token':token},cache:'no-store'};
  if(data!==undefined){options.method='POST';options.headers['Content-Type']='application/json';options.body=JSON.stringify(data);}
  const response=await fetch(path,options);
  const body=await response.json();
  if(!response.ok)throw new Error(typeof body.error==='string'?body.error:(body.error?.message||body.message||`İşlem tamamlanmadı (${response.status}).`));
  return body;
}
function taskWords(task){return task.current_words||task.latest_words||task.original_words||'';}
function title(task){const value=taskWords(task).split('\n')[0];return value.length>110?value.slice(0,107)+'…':value;}
function renderList(){
  const query=$('search').value.toLocaleLowerCase('tr');const list=$('task-list');list.replaceChildren();
  const visible=tasks.filter(t=>(taskWords(t)+' '+t.id).toLocaleLowerCase('tr').includes(query));
  $('task-count').textContent=`${tasks.length} iş · ${tasks.filter(t=>!['completed','cancelled'].includes(t.status)).length} açık`;
  for(const task of visible){const b=node('button',undefined,'task-item'+(current?.id===task.id?' active':''));b.type='button';b.append(node('span',title(task)),node('small',statuses[task.status]||task.status));b.onclick=()=>selectTask(task.id).catch(e=>notice(e.message,true));list.append(b);}
  if(!visible.length)list.append(node('p',tasks.length?'Aramaya uyan iş yok.':'Henüz iş yok.','muted'));
}
function renderTask(){
  $('empty').hidden=true;$('task-detail').hidden=false;$('task-id').textContent=current.id;
  $('task-title').textContent=title(current);$('task-status').textContent=statuses[current.status]||current.status;
  $('current-words').textContent=taskWords(current);$('original-words').textContent=current.original_words;
  $('revision-note').textContent=`Sürüm ${current.revision} · Özgün söz ve önceki sürümler geçmişte korunur.`;
  $('criteria').replaceChildren(...(current.criteria||[]).map(c=>node('li',typeof c==='string'?c:c.description)));
  $('revised-words').value=taskWords(current);
  const auth=$('authority');auth.replaceChildren();for(const [label,value] of [['Söyleyen',current.authority?.actor],['Kaynak',current.authority?.source],['Kapsam',current.authority?.scope]])auth.append(node('dt',label),node('dd',value||'Belirtilmedi'));
  const sources=$('sources');sources.replaceChildren();for(const source of current.sources||[]){const row=node('div',undefined,'source-item');row.append(node('strong',source.name||source.original_path||source.path||source.id),node('p',source.note||'Bu iş için saklanan kaynak sürümü.','muted'),node('code',source.sha256||''));sources.append(row);}if(!sources.childNodes.length)sources.append(node('p','Bu işe dosya kaynağı eklenmedi.','muted'));
  const progress=$('progress');progress.replaceChildren();
  const attempt=(current.attempts||[]).find(a=>a.id===current.active_attempt_id);
  if(attempt)progress.append(node('p',`${attempt.participant} · ${attempt.session_id}`));
  const results=current.results||[];const result=results.find(r=>r.id===current.current_result_id)||results.at(-1);
  if(result){progress.append(node('p',result.summary,'prose'));if(result.id!==current.current_result_id)progress.append(node('p','Bu sonuç önceki çalıştırmaya aittir; güncel işi kapatmaz.','muted'));}
  else progress.append(node('p',attempt?'Atama kayıtlı. Hedef oturumun alımını ve somut sonucunu bekliyor.':'İş hazır. Bir oturuma atanabilir; kaynak paketi devir görünümünde bulunur.','muted'));
  $('pause-task').disabled=!['ready','running','awaiting_verification','blocked'].includes(current.status);
  $('resume-task').disabled=current.status!=='paused'||!runtimeReady;$('cancel-task').disabled=['completed','cancelled'].includes(current.status);
  for(const form of [$('revise-form'),$('assign-form')])for(const field of form.elements)field.disabled=['completed','cancelled'].includes(current.status)||!runtimeReady;
  showView(activeView);renderList();
}
function showView(view){activeView=view;for(const name of ['work','sources','history'])$(`${name}-view`).hidden=name!==view;document.querySelectorAll('[data-view]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.view===view)));}
async function selectTask(id){
  const selected=++selection;
  const [task,bundle,history]=await Promise.all([api(`/api/tasks/${encodeURIComponent(id)}`),api(`/api/tasks/${encodeURIComponent(id)}/context`),api(`/api/tasks/${encodeURIComponent(id)}/events`)]);
  if(selected!==selection)return;
  current=task;context=bundle;$('context').textContent=JSON.stringify(bundle,null,2);const events=Array.isArray(history)?history:(history.events||[]);
  $('events').replaceChildren(...events.map(event=>{const li=node('li');li.append(node('strong',event.kind||event.type||event.event_type||'Olay'),node('time',event.recorded_at||event.at||event.created_at||''));const data=event.data||event.payload;if(data){const d=node('details');d.append(node('summary','Ayrıntı'),node('pre',JSON.stringify(data,null,2)));li.append(d);}return li;}));
  renderTask();
}
async function refresh(){
  const [data,runtime]=await Promise.all([api('/api/tasks'),api('/api/runtime')]);
  runtimeReady=runtime.ready===true;$('new-task').disabled=!runtimeReady;
  $('runtime').textContent=runtime.kernel_verified===true?'NT çekirdek uç noktası doğrulandı · İş yürütümü kullanıcı kipinde':runtime.backend==='portable'?'Taşınabilir geliştirme kipi · NT çekirdek bağlantısı yok':'NT çekirdek bağlantısı doğrulanmadı · Yeni çalışma engellendi';
  tasks=Array.isArray(data)?data:(data.tasks||[]);renderList();if(current)await selectTask(current.id);
}
async function update(action,data){if(!current)return;await api(`/api/tasks/${encodeURIComponent(current.id)}/${action}`,{...data,expected_revision:current.revision,request_key:key()});await refresh();notice('İş kaydı güncellendi.');}
document.querySelectorAll('[data-view]').forEach(b=>b.onclick=()=>showView(b.dataset.view));
$('search').oninput=renderList;$('refresh').onclick=()=>refresh().catch(e=>notice(e.message,true));
$('new-task').onclick=()=>{$('create-error').hidden=true;$('create-dialog').showModal();};$('close-dialog').onclick=()=>$('create-dialog').close();
$('create-form').onsubmit=async(event)=>{
  event.preventDefault();const button=event.submitter;button.disabled=true;
  const payload={original_words:$('new-words').value,authority:{actor:'Haluk',source:'deus_ex_machina yerel kullanıcı girdisi',scope:$('new-scope').value},criteria:lines($('new-criteria').value),sources:lines($('new-sources').value)};
  const signature=JSON.stringify(payload);if(!pendingCreate||pendingCreate.signature!==signature)pendingCreate={signature,key:key()};
  try{const task=await api('/api/tasks',{...payload,request_key:pendingCreate.key});pendingCreate=null;$('create-dialog').close();$('create-form').reset();await refresh();await selectTask(task.id);notice('İş oluşturuldu. Özgün söz ve kapsam kaydedildi.');}catch(error){$('create-error').textContent=error.message;$('create-error').hidden=false;}finally{button.disabled=false;}
};
$('revise-form').onsubmit=async(event)=>{event.preventDefault();try{await update('revise',{original_words:$('revised-words').value});}catch(e){notice(e.message,true);}};
$('assign-form').onsubmit=async(event)=>{event.preventDefault();try{await update('assign',{participant:$('participant').value,session_id:$('session').value,expected_active_attempt_id:current?.active_attempt_id||null});}catch(e){notice(e.message,true);}};
for(const [id,action] of [['pause-task','pause'],['resume-task','resume'],['cancel-task','cancel']])$(id).onclick=()=>update('control',{action}).catch(e=>notice(e.message,true));
$('download-context').onclick=()=>{if(!context)return;const blob=new Blob([JSON.stringify(context,null,2)+'\n'],{type:'application/json'});const url=URL.createObjectURL(blob);const a=node('a');a.href=url;a.download=`deus-${current.id}-s${current.revision}.json`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
async function start(){if(!token){$('runtime').textContent='Yerel başlatma bağlantısı gerekli';$('new-task').disabled=true;notice('Sunucuyu başlattığın terminaldeki launch_url bağlantısını aç. Erişim anahtarı bu sayfadan alınamaz.');return;}try{await refresh();}catch(error){$('runtime').textContent='Çalışma ortamına bağlanılamadı';$('new-task').disabled=true;notice(error.message,true);}}
start();
