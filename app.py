from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)


# Routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Start The App
if __name__ == '__main__':
    app.run(debug=True)
