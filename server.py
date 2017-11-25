from flask import Flask, render_template, request, url_for, redirect
from flask.ext.socketio import SocketIO, emit, join_room


# need some sort of auth library
app = Flask(__name__)


# Routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

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
    app.run(debug=True)
