from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
# from flask import Flask

# app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Yuto'}
    post = [
        {
            'author':{'username':'YUOO'},
            'body':'Beautiful day in Portland'
        },
        {
             'author':{'username':'Candy'},
            'body':'The Avengers movie was so cool!!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts = post)

@app.route('/login', methods=[ 'GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# if __name__ == '__main__':
#     app.run(debug=True)