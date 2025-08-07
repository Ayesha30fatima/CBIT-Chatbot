function appendMessage(sender, message) {
    const chatBox = document.getElementById("chat-box");
    const bubble = document.createElement("div");
    bubble.classList.add("chat-bubble");
    bubble.classList.add(sender === "user" ? "user-bubble" : "bot-bubble");
    bubble.innerHTML = message.replace(/\n/g, "<br>");
    chatBox.appendChild(bubble);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message) return;
    appendMessage("user", message);
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => {
        appendMessage("bot", data.response);
    });
}

function submitContext() {
    const course = document.getElementById("course-code").value.trim();
    const year = document.getElementById("year").value.trim();
    if (!course || !year) return alert("Please fill in both fields.");

    fetch("/set_context", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ course, year })
    })
    .then(() => {
        document.getElementById("context-modal").style.display = "none";
    });
}
