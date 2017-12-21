#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午3:29
# @Author  : tracy
# @Site    : 
# @File    : map_sort.py
# @Software: IntelliJ IDEA

#排序

import sys

baseCount=10000

for line in sys.stdin:
    ss=line.strip().split('\t')
    key = ss[0]
    val = ss[1]

    newKey=baseCount+int(key)

    print "%s\t%s" % (newKey,val)
