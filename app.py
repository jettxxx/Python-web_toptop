from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/<username>')
def user(username):
    return render_template('user.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
