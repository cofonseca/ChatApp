document.addEventListener('DOMContentLoaded', function() {
    var socket = io.connect('127.0.0.1:5000');

    socket.on('connect', function() {
        socket.send('Client has connected!');
    });
});