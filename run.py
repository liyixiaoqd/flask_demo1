# -*- coding:utf-8 -*-
#!flask/bin/python

from app import app
app.debug = True
app.run(host='0.0.0.0',port=5000)   #这样用来监听所有的ip，团队调试用
