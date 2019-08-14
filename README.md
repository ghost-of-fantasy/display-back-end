# display-back-end
展示模块的后端部分

## 安装(开发环境)

```shell script
$ python manage.py makemigrations # 创建初始迁移
$ python manage.py migrate # 数据库据迁移
$ python manage.py runserver  0.0.0.0:8000 --settings=display.settings # 运行
$ python manage.py createsuperuser # 创建超级用户
$ python manage.py seed api --number=15 # 生成假数据
```

> 密码：dgutdev#

## 参考文章
- [django-seed 用于生成假数据](https://github.com/Brobin/django-seed)
- [编写自定义 django-admin 命令](https://docs.djangoproject.com/zh-hans/2.2/howto/custom-management-commands/)