# 此项目用来学习部署Python Web程序

# 使用Supervisor和Gunicorn部署

# 依赖安装
```shell
pip install gunicorn
pip install django
pip install supervisor
```

# 本地服务启动命令
```python
gunicorn -b 0.0.0.0:8001 deploy.wsgi -k gevent -w 2                                                                                                                             
```

# docker启动命令
```shell
docker-compose up -d
```
> 目前项目代码挂在外，但改动后需要重新启动服务才会生效。