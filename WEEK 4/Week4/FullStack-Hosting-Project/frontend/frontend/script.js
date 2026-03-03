function getMessage() {
    fetch("https://YOUR_RENDER_BACKEND_URL/api/message")
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText = data.message;
    });
}
