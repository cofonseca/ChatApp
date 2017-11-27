document.addEventListener('DOMContentLoaded', function() {

    // Connect to the server
    var socket = io.connect(window.location.host);

    // Focus and move cursor to input field
    var input = document.getElementById('userMessage')
    input.focus()
    input.select()

    // When client conects, send a message to the server.
    socket.on('connect', function() {
        socket.send('Client has connected!');
    });

    // When message gets sent, append it to the screen
    socket.on('message', function(msg) {
        var messageArea = document.getElementById('messageArea');
        var messageLine = document.createElement("li");
        messageLine.appendChild(document.createTextNode(userId + ': ' + msg));
        messageArea.appendChild(messageLine);
    });


    var sendButton = document.getElementById('send');

    // When message gets sent, send it to the server and clear the input field
    sendButton.addEventListener('click', function() {
        var msg = document.getElementById('userMessage')
        socket.send(msg.value)
        msg.value = ''
    });

    // When the enter key is pressed, click the button
    input.addEventListener('keyup', function(event) {
        event.preventDefault();
        if (event.keyCode === 13) {
            sendButton.click();
        };
    });

});