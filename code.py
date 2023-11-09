from flask import Flask, render_template, redirect, url_for, flash
from flask_googlelogin import GoogleLogin, GoogleLoggedInAccount

app = Flask(__name__)

app.config['SECRET_KEY'] = '24'
app.config['GOOGLELOGIN_CLIENT_ID'] = 'Hello Bhagyasri'
app.config['GOOGLELOGIN_CLIENT_SECRET'] = 'You signed in with the email address kavitibhagyasrirao@gmail.com'

googlelogin = GoogleLogin(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return googlelogin.login_redirect(request.args.get('next'))

@app.route('/login/callback')
def login_callback():
    try:
        google_user = googlelogin.current_user()
    except Exception as e:
        flash('Authentication failed.')
        return redirect(url_for('home'))

    if google_user.email == 'YOUR_AUTHORIZED_EMAIL':
        flash('Successfully signed in with Google.')
        return redirect(url_for('home'))
    else:
        flash('Failed to sign in with Google.')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
