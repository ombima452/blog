from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI']='sqlite:///blog.db'

db = SQLAlchemy(app)
 
class Blogpost(db.Model):
    
    id =db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')

def post():
    return render_template('post.html') 

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
   
    return render_template('login.html')



# @app.route('/addpost',methods=['POST'])
# def addpost():
     
#     title = request.form['title']
#     subtitle = request.form['subtitle']
#     author = request.form['author']
#     content = request.form['content']
        
#     post = Blogpost(title = title,subtitle = subtitle, author = author,content = content,date_posted = datetime.now())
    
#     # db.session.add(post)
#     # db.session.commit()
    
#     return redirect(url_for('post'))
    
    
# if __name__== '__main__':
#     app.run(debug=True) 