
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from datetime import datetime
from flask import current_app, request, url_for

from app import db


class CommonUserInfo(db.Model):
    """
    用户表
    """
    __tablename__ = 'common_user_info'
    id = db.Column(db.Integer, primary_key=True)
    #账户
    login_account = db.Column(db.String(64),unique=True)
    #密码
    login_password = db.Column(db.String(64))
    #性别
    user_gender = db.Column(db.Integer)
    #真实名称
    user_name = db.Column(db.String(64))
    #用户编号
    user_no = db.Column(db.String(64))
    #所属组织机构
    user_org = db.Column(db.Integer)



    #用户状态
    status = db.Column(db.Integer)
    #操作人
    operate_user_id=db.Column(db.Integer)
    #操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.utcnow)


    def __repr__(self):
        return '<common_user_info %r>' % self.login_account



class CommonRoleInfo(db.Model):
    """
        角色表
    """
    __tablename__ = 'common_role_info'
    id = db.Column(db.Integer, primary_key=True)
    #角色代码
    role_code = db.Column(db.String(64), unique=True)
    #角色名称
    role_name = db.Column(db.String(64), unique=True)
    #角色顺序
    role_order=db.Column(db.Integer)
    #备注
    role_remark=db.Column(db.Text)
    # 用户状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.utcnow)



    def __repr__(self):
        return '<common_role_info %r>' % self.role_name


class CommonOrgInfo(db.Model):
    """
        组织机构表
    """
    __tablename__ = 'common_org_info'
    id = db.Column(db.Integer, primary_key=True)
    #组织机构代码
    org_code = db.Column(db.String(64), unique=True)
    #组织机构全称
    org_fullname = db.Column(db.String(64), unique=True)
    # 组织机构名称
    org_name = db.Column(db.String(64), unique=True)

    #顺序
    org_order=db.Column(db.Integer)
    #父节点编号
    org_pid = db.Column(db.Integer)

    #备注
    role_remark=db.Column(db.Text)

    # 状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.utcnow)



    def __repr__(self):
        return '<common_org_info %r>' % self.role_name





class CommonMenuInfo(db.Model):
    """
        菜单表
    """
    __tablename__ = 'common_menu_info'
    id = db.Column(db.Integer, primary_key=True)
    #菜单样式
    menu_cls = db.Column(db.String(64), unique=True)
    #菜单代码
    menu_code = db.Column(db.String(64), unique=True)

    #菜单级别
    menu_level=db.Column(db.Integer)
    #菜单名称
    menu_name=db.Column(db.String(64))
    #菜单导航
    menu_nav=db.Column(db.String(64))
    #菜单排序
    menu_order=db.Column(db.Integer)
    #父节点
    menu_pid=db.Column(db.String(64))
    #备注
    menu_remark=db.Column(db.String(64))
    #所属系统
    menu_sysid=db.Column(db.String(64))
    #类别
    menu_type=db.Column(db.Integer)
    #url
    menu_url=db.Column(db.String(64))

    # 状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.utcnow)



    def __repr__(self):
        return '<common_org_info %r>' % self.role_name
