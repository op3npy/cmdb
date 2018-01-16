* 命令记录


django 多数据库创建
auth模型 —— User、Group和Permission —— 关联在一起并与ContentType关联，所以它们必须与ContentType存储在相同的数据库中。


先创建数据库
DROP DATABASE IF EXISTS sso ;
CREATE DATABASE IF NOT EXISTS   sso;
DROP DATABASE IF EXISTS resource;
CREATE DATABASE IF NOT EXISTS resource;

以下操作已经集成到自动化命令中, python manage.py db_cmd -h查看用法

python .\manage.py makemigrations resource
python .\manage.py migrate --database resource
python .\manage.py migrate auth --database=sso
python .\manage.py migrate contenttypes --database=sso
python .\manage.py migrate sessions --database=sso
python .\manage.py migrate admin --database=sso


python .\manage.py createsuperuser --database=sso --username=admin --email=none

password=admin123



