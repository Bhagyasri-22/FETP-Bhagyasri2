from flask import Flask, redirect, url_for, render_template_string
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.secret_key = 'Superskrit'

blueprint = make_google_blueprint(
    client_id= '1015024038462-vnhejth1pomsfbjvf4arqe63io6e77mq.apps.googleusercontent.com',
    client_secret= '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',
    scope=['profile', 'email'],
    redirect_to='index',
)
app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def index():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    return resp.text

if __name__ == '__main__':
    app.run()
    
    
