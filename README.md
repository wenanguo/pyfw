CRM 应用简介
======



本应用为基础开发框架，进行相关基础工具的整合


启动命令  python manage.py runserver --host 0.0.0.0


测试命令  python manage.py test


数据库迁移

初始化 python manage.py db init

生成脚本 python manage.py db migrate -m "initial migration"

更新数据库 python manage.py db upgrade

代码性能分析 python manage.py profile  启动，浏览器请求
