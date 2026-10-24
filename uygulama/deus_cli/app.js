'use strict';
const el = id => document.getElementById(id);
const statuses = {queued:'CLI alımı bekleniyor', claimed:'CLI isteği aldı', answered:'Yanıt geldi'};
let active = null, state = null, sending = false;
function node(tag, text, cls) {const n=document.createElement(tag); if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;}
function render() {
  const selected=el('target').value;
  const signature=JSON.stringify(state.sessions.map(s=>[s.id,s.participant,s.label]));
  if(el('target').dataset.signature!==signature){el('target').replaceChildren(...state.sessions.map(s=>new Option(`${s.participant} · ${s.label}`,s.id)));el('target').dataset.signature=signature;}
  if(active) el('target').value=active.session_id; else if(state.sessions.some(s=>s.id===selected)) el('target').value=selected;
  el('target').disabled=!!active;
  el('send').disabled=sending || !state.sessions.length;
  if(!state.sessions.length)el('notice').textContent='Henüz bir CLI oturumu kayıtlı değil.';
  el('jobs').replaceChildren(...state.jobs.map(job=>{
    const b=node('button',`${job.participant} · ${job.turns[0].original_words.slice(0,65)}`,'job'+(active?.id===job.id?' selected':''));
    b.type='button';b.onclick=()=>{active=job;localStorage.setItem('deus_active',job.id);render();};return b;
  }));
  if(!active)return;
  const view=el('conversation');view.replaceChildren(node('p',`${active.participant} · ${active.label} · İş ${active.id.slice(0,8)}`,'muted'));
  for(const turn of active.turns){
    const input=node('article',undefined,'message user');input.append(node('small',`${turn.revision}. ileti · ${statuses[turn.status]}`),node('div',turn.original_words));
    if(turn.source_note)input.append(node('small',turn.source_note,'muted'));view.append(input);
    if(turn.response){
      const answer=node('article',undefined,'message answer');answer.append(node('small',`${active.participant} · CLI karşılığı`),node('div',turn.response));
      if(turn.sources.length){const details=node('details');details.append(node('summary',`Kaynaklar (${turn.sources.length})`));for(const source of turn.sources)details.append(node('p',`${source.name}\nSHA-256: ${source.sha256}\n${source.path}`,'source'));answer.append(details);}
      view.append(answer);
    }
  }
}
async function refresh(){
  const response=await fetch('/api/state');if(!response.ok)throw new Error('Arayüze erişilemiyor.');state=await response.json();
  const id=active?.id || localStorage.getItem('deus_active');active=state.jobs.find(j=>j.id===id)||null;render();
}
async function submit(payload){
  const response=await fetch('/api/messages',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
  const result=await response.json();if(!response.ok)throw new Error(result.error||'İstek gönderilemedi.');
  active=result;localStorage.setItem('deus_active',result.id);localStorage.removeItem('deus_pending');el('words').value='';el('notice').textContent='İstek kaydedildi; CLI alımı bekleniyor.';await refresh();
}
el('compose').addEventListener('submit',async event=>{
  event.preventDefault();if(sending)return;sending=true;el('send').disabled=true;
  const pending=JSON.parse(localStorage.getItem('deus_pending')||'null');
  const payload=pending || {session_id:el('target').value,words:el('words').value,request_key:crypto.randomUUID(),job_id:active?.id||null};
  localStorage.setItem('deus_pending',JSON.stringify(payload));
  try{await submit(payload);}catch(error){el('notice').textContent=error.message+' Aynı isteği yeniden gönderebilirsin.';}finally{sending=false;el('send').disabled=!state?.sessions.length;}
});
el('new').onclick=()=>{if(localStorage.getItem('deus_pending')){el('notice').textContent='Önce bekleyen gönderimin sonucunu al.';return;}active=null;localStorage.removeItem('deus_active');el('conversation').replaceChildren(node('h2','Yeni istek'));el('words').value='';el('notice').textContent='';render();};
refresh().then(async()=>{const pending=JSON.parse(localStorage.getItem('deus_pending')||'null');if(pending)await submit(pending);}).catch(error=>{el('notice').textContent=error.message;});
setInterval(()=>refresh().catch(error=>{el('notice').textContent=error.message;}),2000);
