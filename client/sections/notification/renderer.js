const { ipcRenderer } = require('electron');


function notifyDesktop(message, sender) {
    new Notification('New WUPHF from' + sender, {
      body: message
    });
  }

function speakAloud(message, sender) {
    var utter = new SpeechSynthesisUtterance();
    utter.rate = 1;
	utter.pitch = 0.5;
    utter.text = 'You have a new woof from ' + sender + '. ' + message;
    window.speechSynthesis.speak(utter);
}

ipcRenderer.on('message-received', function(event, data){
    document.getElementById("sender").innerHTML = data.sender;
    document.getElementById("message").innerHTML = data.message;
    notifyDesktop(data.message, data.sender);
    speakAloud(data.message, data.sender);
});
