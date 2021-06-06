let socket = new WebSocket("ws://127.0.0.1:9000/web_socket");

socket.onmessage = function(event) {
  alert(`[message] Data received from server: ${event.data}`);
};

socket.onclose = function(event) {
  if (event.wasClean) {
    alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    alert('[close] Connection died');
  }
};

socket.onerror = function(error) {
  alert(`cannot connect to server`);
};

function sendEchoMessage() {
  const ctrlMessage = {
    command: 'echo',
    parameter: document.getElementById('printContent').value
  };
  socket.send(JSON.stringify(ctrlMessage));
  output.innerText = 'Message sent';
}