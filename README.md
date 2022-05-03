# 此项目用来学习部署Python Web程序

# 使用Supervisor和Gunicorn部署

# 依赖安装
```shell
pip install gunicorn
pip install django
pip install supervisor
```

# 服务启动命令
```python
gunicorn -b 0.0.0.0:8001 deploy.wsgi -k gevent -w 2                                                                                                                             
```