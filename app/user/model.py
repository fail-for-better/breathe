# -*- coding:utf-8 -*-
# @Author : 王博
# @Time : 2021/11/26 17:07
# Design: Promission-Control by Role-Based-Access Control
# Reference: https://www.cnblogs.com/RudeCrab/p/14251274.html
from app import db
from app.utils.base_models import BaseModel
from flask_login import UserMixin, login_user
from werkzeug.security import check_password_hash, generate_password_hash

user_role_table = db.Table(
    'user_role',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)
role_permission_table = db.Table(
    'role_permission',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
)


class User(BaseModel, UserMixin):

    __tablename__ = 'user'

    username = db.Column(db.String(80),unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120))
    brief = db.Column(db.String(180))
    picture = db.Column(db.String(50),)
    # role = db.relationship('Role')

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(pwhash, password)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Role(BaseModel):

    __tablename__ = 'role'

    name = db.Column(db.String(50), nullable=False, unique=True)
    # permission = db.relationship('Permission')

    def __repr__(self):
        return '%s' % self.name


class Permission(BaseModel):

    __tablename__ = 'permission'

    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return '%s' % self.name
