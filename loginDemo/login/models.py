from django.db import models

# Create your models here.
# Django自带sqlite3数据库，Django自动创建的db.sqlite3文件数据库
#在settings.py里找到DATABASEE,去配置就行
#存到数据库
class User(models.Model):
    #定义表字段

    #用户名不能长度，数据库得限制死,unique唯一约束，自动加上约束
    username = models.CharField(max_length=128,unique=True)#字符串类型，且最大长度
    #设置最大长度就行
    password = models.CharField(max_length=256)

''''
创建了数据库
1.python3 manage.py makemigrations 数据库数据同步，驱动起来
igrations for 'login':
  login/migrations/0001_initial.py
    - Create model User
2. python3 manage.py migrate  在数据里创建我们自己的数据或者表格
   出现这个信息代表创建成功:Applying login.0001_initial.
3.启动数据库，
 更改浏览器地址为:
 http://127.0.0.1:8000/admin/login/?next=/admin/
 可以在里面做一些增删改查
4. 创建管理员
 python3 manage.py createsuperuser
5 名字就叫zoujunping admin
6 email 随便写:admin@admin. test
7 密码： 1234567890qaz
8 再次密码:1234567890qaz
9 Superuser created successfully显示超级管理员窗户创造成功
10 再去http://127.0.0.1:8000/admin/login/?next=/admin/页面登录
11.点击Add Users添加账户密码
   这里我自定义
   账号:sougouid
   密码：qazwsxed

12点击Save保存   
13 显示User object(1)
14 在views.py验证用户密码是否正确
'''