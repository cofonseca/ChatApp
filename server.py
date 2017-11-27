from flask import Flask, render_template, request, url_for, redirect
from flask_socketio import SocketIO, send


# need some sort of auth library
app = Flask(__name__)
app.config['SECRET_KEY'] = 's3cr3tk3y'
socketio = SocketIO(app)


# Routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    userId = request.form.get('userId')
    print(userId)
    return render_template('chat.html', userId=userId)

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)
    #broadcast=False could be used for 1:1 private chatting

# /chat/
# redirect to /chat/general
# requires login

# /chat/<roomname>
# redirect to /chat/name of room
# requires login

# /user/<username>
# redirect to user profile
# requires login

# /login


# Start The App
if __name__ == '__main__':
    socketio.run(app)
