const speakBtn = document.getElementById("speak-btn");
const output = document.getElementById("output");

speakBtn.addEventListener("click", () => {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";
  recognition.start();

  recognition.onresult = (event) => {
    const command = event.results[0][0].transcript;
    output.textContent = `You said: ${command}`;

    // Send command to backend
    fetch("/process", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command })
    })
      .then((response) => response.json())
      .then((data) => {
        output.textContent = data.response;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };
});
