from datetime import datetime
from app import db

"""
权限系统 RBAC
todo: some table use UUID?
"""

Role_Permission = db.Table(
    'role_permission',
    db.Column('role_id', db.Integer, db.ForeignKey('role.role_id'), primary_key=True, nullable=False),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.permission_id'), primary_key=True, nullable=False)
)


class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    permission_id = db.relationship(
        'Permission',
        secondary=Role_Permission,
        lazy="subquery",
        backref=db.backref('roles', lazy=True)
    )

    def __repr__(self):
        return '<Role %r>' % self.name


class Object(db.Model):
    object_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    object_name = db.Column(db.String(50), unique=True, nullable=False)


class Permission(db.Model):
    permission_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    permission_name = db.Column(db.String(50), unique=True, nullable=False)
    object_id = db.Column(db.Integer, db.ForeignKey('object.object_id'), nullable=False)

    operations = db.Column(db.String(50), nullable=False, default='crud')

    def __repr__(self):
        return '<Permission %r>' % self.name


# class Session(db.Model):
#     pass


User_Role = db.Table(
    'user_role',
    db.Column('role_id', db.Integer, db.ForeignKey('role.role_id'), primary_key=True, nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'), primary_key=True, nullable=False)
)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=True)
    sex = db.Column(db.Integer, nullable=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    role_id = db.relationship(
        'Role',
        secondary=User_Role,
        lazy="subquery",
        backref=db.backref('users', lazy=True)
    )

    def __repr__(self):
        return '<User %r>' % self.username
