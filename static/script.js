const socket = io.connect("http://" + document.domain + ":" + location.port);
const room = "general";

socket.on("connect", () => {
    socket.emit("join", { room: room });
});

socket.on("message", (data) => {
    const msgDiv = document.createElement("div");
    msgDiv.className = "message";
    msgDiv.textContent = data.msg;
    document.getElementById("messages").appendChild(msgDiv);
    // Auto-scroll to bottom
    document.getElementById("messages").scrollTop = document.getElementById("messages").scrollHeight;
});

document.getElementById("send-btn").addEventListener("click", () => {
    const msgInput = document.getElementById("message-input");
    const message = msgInput.value.trim();
    if (message) {
        socket.emit("message", { msg: message, room: room });
        msgInput.value = "";
    }
});

// Send message on Enter key
document.getElementById("message-input").addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        e.preventDefault();
        document.getElementById("send-btn").click();
    }
});