# 命令记录


`django 多数据库创建
auth模型 —— User、Group和Permission —— 关联在一起并与ContentType关联，所以它们必须与ContentType存储在相同的数据库中。
`


## 以下操作已经集成到自动化命令中
python manage.py db_cmd -h查看用法
更改了模型代码后（增删改表字段等）， python manage.py db_cmd --rebuild


## 参考创建管理员用户
python .\manage.py createsuperuser --database=sso --username=admin --email=none

password=admin123


运行ws服务器 daphne  -b 0.0.0.0 -p 8001 cmdb.asgi:application