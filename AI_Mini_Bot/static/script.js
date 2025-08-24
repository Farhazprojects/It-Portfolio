const chat = document.getElementById("chat");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send");

function addBubble(text, who="bot"){
  const div = document.createElement("div");
  div.className = `bubble ${who}`;
  div.textContent = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
  return div;
}

function addTyping(){
  const div = document.createElement("div");
  div.className = "bubble bot";
  const t = document.createElement("span");
  t.className = "typing";
  t.innerHTML = "<span>●</span> <span>●</span> <span>●</span>";
  div.appendChild(t);
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
  return div;
}

async function sendMessage(){
  const text = input.value.trim();
  if(!text) return;
  addBubble(text, "user");
  input.value = "";
  autosize();

  sendBtn.disabled = true;
  const typing = addTyping();
  try{
    const res = await fetch("/chat", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({message: text})
    });
    const data = await res.json();
    typing.remove();
    addBubble(data.reply, "bot");
  }catch(e){
    typing.remove();
    addBubble("Oops, network error. Try again.", "bot");
  }finally{
    sendBtn.disabled = false;
    input.focus();
  }
}

sendBtn.addEventListener("click", sendMessage);
input.addEventListener("keydown", (e)=>{
  if(e.key === "Enter" && !e.shiftKey){
    e.preventDefault();
    sendMessage();
  }
});

// Auto-size textarea
function autosize(){
  input.style.height = "auto";
  input.style.height = Math.min(200, input.scrollHeight) + "px";
}
input.addEventListener("input", autosize);
autosize();

// Welcome system message
(function(){
  const sys = document.createElement("div");
  sys.className = "bubble sys";
  sys.textContent = "MiniBot is a mini project of Farhaz Khondoker. It is session-based and remembers your name/mood until you say 'bye' or refresh.";
  chat.appendChild(sys);
})();