from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    return render_template('user.html', user_name="Nguyen Duc Nhat")

if __name__ == '__main__':
    app.run()
