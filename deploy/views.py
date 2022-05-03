# -*- coding: UTF-8 -*-
"""
@Author : Sydove
@Project ：deploy 
@Time : 2022/5/3 14:33 
@File : views.py
@attention:
"""
from django.views import View
from django.http import HttpResponse


class Test(View):
    def get(self,request):
        return HttpResponse("<h1>Hello World! </h1>")