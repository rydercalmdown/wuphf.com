// Modules to control application life and create native browser window
const {app, BrowserWindow} = require('electron');
const path = require('path');
var request = require('request');


function createWindow () {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    show: false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })
  mainWindow.loadFile('index.html')
}

app.whenReady().then(() => {
  createWindow()
  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

function openMessageReceivedWindow(data) {
  var messageReceivedWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    },
  })
  messageReceivedWindow.loadFile('sections/notification/index.html')
  messageReceivedWindow.webContents.once('dom-ready', () => {
    messageReceivedWindow.send('message-received', data);
    const options = { silent: true, deviceName: 'Closet' }
    messageReceivedWindow.webContents.print(options, (success, errorType) => {
      if (!success) console.log(errorType)
    })
  });
}

function messageReceived(wuphfId) {
  // A message was received
  console.log(wuphfId);
  request.get({
    url: 'https://example.com/api/details/?id=' + wuphfId,
    json: true,
    headers: {'User-Agent': 'request'}
  }, (err, res, data) => {
    if (err) {
      return;
    } else if (res.statusCode !== 200) {
      return;
    } else {
      // data
      console.log('message');
      console.log(data.message);
      console.log('sender');
      console.log(data.sender);
      openMessageReceivedWindow(data);
    }
});
}


function checkForNewMessage() {
  request.get({
      url: 'https://example.com/api/list/',
      json: true,
      headers: {'User-Agent': 'request'}
    }, (err, res, data) => {
      if (err) {
        return;
      } else if (res.statusCode !== 200) {
        return;
      } else {
        if (data.wuphfs === undefined || data.wuphfs.length == 0) {
          return
        } else {
          messageReceived(data.wuphfs[0]);
        }
      }
  });
}


function listenForNewMessages() {
  // Listens for new WUPHF messages
  setInterval(function(){ checkForNewMessage(); }, 1000);
}


listenForNewMessages();
