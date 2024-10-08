from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self,key,address):
        if address == '':
            raise ValueError("Name should not be empty")
        authors=Author.query.filter_by(name=address).first()
        if authors:
            raise ValueError("Name must be unique")
        return address
    @validates('phone_number')
    def validates_phone_number(self,key,address):
        if len(address) == 10 and address.isdigit():
            return address
        raise ValueError("Phone number must have 10 digits")

    
    
   
    

            
        
            

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    CLICKBAIT_PHRASES = ["Won't Believe", "Secret", "Top", "Guess"]

    @validates('content')
    def validates_content(self,key,address):
        if len(address) >= 250:
            return address
        raise ValueError("Post content is at least 250 characters long")
    @validates('summary')
    def validates_summary(self,key,address):
        if len(address) <= 250:
            return address
        raise ValueError ("Post summary is a maximum of 250 characters.")
    
    @validates('title')
    def validates_title(self,key,address):
        if any(word in address for word in self.CLICKBAIT_PHRASES):
            return address
        raise ValueError("Must contain the following phrases,Wont Believe,Secret,Top, Guess")
      
    @validates('category')
    def validates_category(self,key,address):
        valid_list=['Fiction','Non-Fiction']
        if address in valid_list:
            return address
        raise ValueError('category has to be either Fiction or Non fiction')
    
        




   

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
