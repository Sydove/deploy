FROM python:3.7.5

WORKDIR /root/deploy

ADD ./requirements.txt /root/deploy

RUN pip install -r requirements.txt -i https://pypi.douban.com/simple/