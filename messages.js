
document.addEventListener("DOMContentLoaded", function() {
    const messageList = document.getElementById("messageList");
    const sendMessageForm = document.getElementById("sendMessageForm");

    sendMessageForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const recipient = document.getElementById("recipient").value;
        const message = document.getElementById("message").value;

        console.log("Sending message...");
        console.log("Recipient:", recipient);
        console.log("Message:", message);

        const messageItem = document.createElement("div");
        messageItem.classList.add("message-item");
        messageItem.innerHTML = `
      <strong>${recipient}:</strong> ${message}
    `;
        messageList.appendChild(messageItem);

        sendMessageForm.reset();
    });
});

function backButton() {
    window.history.back();
}