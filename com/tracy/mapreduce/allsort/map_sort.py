#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午4:09
# @Author  : tracy
# @Site    : 
# @File    : map_sort.py
# @Software: IntelliJ IDEA

#小于10000的数据存入在一个partion文件中

import sys

baseCount=10000

for line in sys.stdin:
    ss=line.strip().split('\t')
    key=ss[0]
    val=ss[1]

    newKey=baseCount+int(val)

    red_idx =1

    if newKey < (10100+10000) /2:
        red_idx=0

    print "%s\t%s\t%s" % (red_idx,newKey,val)