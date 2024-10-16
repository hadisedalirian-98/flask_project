from blog import db, app, login_manager,render_template 
from datetime import datetime
from flask_login import UserMixin  

@login_manager.user_loader  
def load_user(user_id):   
    return User.query.get(int(user_id))  

class User(db.Model, UserMixin):  
    id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(30), unique=True, nullable=False)  
    email = db.Column(db.String(60), unique=True, nullable=False)  
    password = db.Column(db.String(60), nullable=False)  
    posts = db.relationship('Post', backref='author', lazy=True)  

    def __repr__(self):  
        # نمایش کاربر  
        return f'User(username={self.username}, email={self.email})'  

class Post(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(120), nullable=False)  
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)  # اصلاح این خط  
    content = db.Column(db.Text, nullable=False)  
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # اصلاح ForeignKey  

    def __repr__(self):  
        date_time = self.date.strftime('%Y-%M-%d %H:%M:%S')
        # نمایش پست  
        return f'Post(id={self.id}, title={self.title[:30]}, date={date_time})'