from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    create_date = db.Column(db.DateTime(), nullable=False)
    vacation = db.relationship('Vacation', backref='account', uselist=False)
    post = db.relationship('Post', backref='account', lazy=True)


class Vacation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)
    used = db.Column(db.Integer)
    account_id = db.Column(db.Integer(), db.ForeignKey('account.id'))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    approver = db.Column(db.String(50), nullable=False)
    account_id = db.Column(
                    db.Integer,
                    db.ForeignKey('account.id'),
                    nullable=False)
