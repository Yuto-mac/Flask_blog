
from turtle import title
from flask import render_template
from app import app
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

# if __name__ == '__main__':
#     app.run(debug=True)