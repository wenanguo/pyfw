from lib2to3.pytree import Base

from flask_login import UserMixin, AnonymousUserMixin
from sqlalchemy import Table, Column, Integer, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask import current_app, request, url_for

from init import db, login_manager

#用户角色多对多关系表
from pyfw.util import JsonUtil

user_role_mapper = db.Table('common_user_roles',
                         db.Column('user_id', db.Integer, db.ForeignKey('common_user_info.id') , nullable=False, primary_key=True),
                         db.Column('role_id', db.Integer, db.ForeignKey('common_role_info.id') , nullable=False, primary_key=True)
                         )


#用户组织多对多关系表
user_org_mapper = db.Table('common_user_org',
                         db.Column('user_id', db.Integer, db.ForeignKey('common_user_info.id') , nullable=False, primary_key=True),
                         db.Column('org_id', db.Integer, db.ForeignKey('common_org_info.id') , nullable=False, primary_key=True)
                         )





class CommonUserInfo(UserMixin,db.Model):
    """
    用户表
    """
    __tablename__ = 'common_user_info'

    id = db.Column(db.Integer, primary_key=True)
    # 账户
    login_account = db.Column(db.String(64), unique=True)
    # 密码
    login_password = db.Column(db.String(128))
    # 真实名称
    user_name = db.Column(db.String(64))
    # 用户编号
    user_no = db.Column(db.String(64))
    # 账号状态
    user_status = db.Column(db.String(64))
    # 所属系统
    user_sys = db.Column(db.String(64))
    # 手机号
    user_phone = db.Column(db.String(64))
    # 用户分类（1：内部人员；2：外部人员）
    user_type = db.Column(db.String(64))
    # 备注
    user_remark = db.Column(db.String(64))
    # 用户性别（1:男性，0:女性）
    user_sex = db.Column(db.String(64))
    # 性别
    user_gender = db.Column(db.Integer)
    # 邮箱
    user_email = db.Column(db.String(64))
    # 所属组织机构
    user_org = db.Column(db.Integer)

    # extend
    # 真实头像
    user_icon = db.Column(db.String(64))

    # 最后登录时间
    last_login = db.Column(db.DateTime(), default=datetime.now)

    # 用户状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.now)

    roles = db.relationship('CommonRoleInfo',
                            secondary=user_role_mapper,
                            lazy='dynamic',
    backref = db.backref('users', lazy='dynamic')
    )

    orgs = db.relationship('CommonOrgInfo',
                            secondary=user_org_mapper,
                            lazy='dynamic',
                            backref=db.backref('users', lazy='dynamic')
                            )


    def __repr__(self):
        return '<common_user_info %r>' % self.__dict__

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.login_password = generate_password_hash(password)

    def verify_password(self, password):
        """
        密码验证方法
        :param password: 需要验证的密码
        :return:
        """
        return check_password_hash(self.login_password, password)

    @login_manager.user_loader
    def load_user(user_id):
        return CommonUserInfo.query.get(int(user_id))

    def to_json(self):

        return JsonUtil.ObjToJson(self)

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError

        from random import seed
        import forgery_py
        seed()
        for i in range(count):
            u = CommonUserInfo(user_email=forgery_py.internet.email_address(),
                               login_account=forgery_py.internet.user_name(True),
                               login_password=forgery_py.lorem_ipsum.word(),
                               icon="images/2.jpg"
                                )
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()






class CommonRoleInfo(db.Model):
    """
        角色表
    """
    __tablename__ = 'common_role_info'
    id = db.Column(db.Integer, primary_key=True)
    #角色代码
    role_code = db.Column(db.String(64), unique=True)
    #角色名称
    role_name = db.Column(db.String(64))
    #角色顺序
    role_order=db.Column(db.Integer)
    #备注
    role_remark=db.Column(db.Text)
    # 角色装
    role_status = db.Column(db.Integer)
    # 所属系统
    sys_id = db.Column(db.Integer)

    # 用户状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.now)



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
    # 组织机构名称
    org_name = db.Column(db.String(64), unique=True)
    #组织机构全称
    org_fullname = db.Column(db.String(64), unique=True)

    # 节点状态
    org_status = db.Column(db.Integer)

    org_area_id = db.Column(db.String(64))

    org_remark = db.Column(db.String(200))
    # 父节点编号
    org_parent_id = db.Column(db.Integer)
    # 排序
    org_sort  = db.Column(db.Integer)

    # 机构类别
    org_type  = db.Column(db.Integer)





    # 状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.now)





    def __repr__(self):
        return '<common_org_info %r>' % self.org_name





class CommonMenuInfo(db.Model):
    """
        菜单表
    """
    __tablename__ = 'common_menu_info'
    id = db.Column(db.Integer, primary_key=True)
    # 菜单代码
    menu_code = db.Column(db.String(64), unique=True)
    # 菜单名称
    menu_name = db.Column(db.String(64))
    # 菜单导航
    menu_nav = db.Column(db.String(64))
    # 备注
    menu_remark = db.Column(db.String(64))
    # url
    menu_url = db.Column(db.String(64))
    #菜单样式
    menu_cls = db.Column(db.String(64), unique=True)


    #菜单级别
    menu_level=db.Column(db.Integer)
    # 类别
    menu_type = db.Column(db.Integer)


    #菜单排序
    menu_order=db.Column(db.Integer)
    # 状态
    menu_status = db.Column(db.Integer)
    #父节点
    menu_pid=db.Column(db.String(64))
    #是否隐藏
    menu_hidden = db.Column(db.Integer)
    #布局
    menu_use_sys_layout = db.Column(db.Integer)
    #目标
    menu_target = db.Column(db.String(64))
    # 所属系统
    menu_sysid = db.Column(db.String(64))
    #spt
    menu_spt = db.Column(db.String(64))





    # 状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.now)



    def __repr__(self):
        return '<common_org_info %r>' % self.role_name



class CommonMenuOptInfo(db.Model):
    """
        菜单操作表
    """
    __tablename__ = 'common_menu_opt_info'
    id = db.Column(db.Integer, primary_key=True)
    #操作编号
    menu_id = db.Column(db.Integer)
    #操作代码
    opt_code = db.Column(db.String(64))
    #操作名称
    opt_name = db.Column(db.String(64))
    #操作url
    opt_url = db.Column(db.String(64))
    #操作方法
    opt_method = db.Column(db.String(64))
    #操作状态
    opt_status = db.Column(db.Integer)
    #操作备注
    opt_remark = db.Column(db.String(64))
    #排序
    opt_order = db.Column(db.Integer)

    # 状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.now)

    def __repr__(self):
        return '<common_org_info %r>' % self.opt_name





class CommonHttpRequestLogs(db.Model):
    """
       http请求日志表
    """
    __tablename__ = 'common_http_request_logs'

    id = db.Column(db.Integer, primary_key=True)

    # 请求流水号
    timestamp = db.Column(db.String(500))
    # 分类
    catalog = db.Column(db.String(50))
    #请求url
    request_url = db.Column(db.String(500))
    #请求数据
    request_data = db.Column(db.Text)
    # 返回状态码
    response_status_code = db.Column(db.String(100))
    # 返回数据
    response_data = db.Column(db.Text)

    # 请求类别 1 外部请求本应用 2 本应用请求外部
    type= db.Column(db.Integer)

    # 开始时间
    start_time= db.Column(db.DateTime(), default=datetime.now)


    # 结束时间
    end_time= db.Column(db.DateTime(), default=datetime.now)

    # 请求耗时
    time_consuming= db.Column(db.String(100))

    # 状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.now)

    def __repr__(self):
        return '<common_http_request_logs %r>' % self.id

    def to_json(self):
        return JsonUtil.ObjToJson(self)


    def start(self,timestamp="20190308000000",catalog="1001",request_url="",type="1",request_data=""):

        self.timestamp=str(timestamp)
        self.catalog = str(catalog)
        self.request_url = str(request_url)
        self.type = str(type)
        self.request_data = str(request_data)
        self.start_time = datetime.now()


    def end(self,response_status_code="200",response_data=""):

        self.response_status_code = response_status_code
        self.response_data = str(response_data)

        self.end_time = datetime.now()
        self.time_consuming = (self.end_time - self.start_time).total_seconds()





class CommonHealth(db.Model):
    """
       健康检查
    """
    __tablename__ = 'common_health'

    id = db.Column(db.Integer, primary_key=True)

    # 请求流水号
    timestamp = db.Column(db.String(500))
    # 分类
    catalog = db.Column(db.String(50))

    #请求数据
    request_data = db.Column(db.Text)
    # 返回状态码
    response_status_code = db.Column(db.String(100))
    # 返回数据
    response_data = db.Column(db.Text)

    # 开始时间
    start_time= db.Column(db.DateTime(), default=datetime.now)

    # 结束时间
    end_time= db.Column(db.DateTime(), default=datetime.now)

    # 请求耗时
    time_consuming= db.Column(db.String(100))

    # 状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.now)

    def __repr__(self):
        return '<common_health %r>' % self.id

    def to_json(self):
        return JsonUtil.ObjToJson(self)


