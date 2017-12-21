#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午3:07
# @Author  : tracy
# @Site    : 
# @File    : map.py
# @Software: IntelliJ IDEA


#map 过程 形成以下数据格式
'''
a 1
b 1
c 1
d 1
e 1
'''

import sys

for line in sys.stdin:
    ss=line.strip().split(' ')
    for s in ss:
        if s.strip() !="":
            print "%s\t%s" % (s,1)