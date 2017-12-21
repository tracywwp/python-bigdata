#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午4:03
# @Author  : tracy
# @Site    : 
# @File    : map_sort.py
# @Software: IntelliJ IDEA

import sys

for line in sys.stdin:
    ss=line.strip().split('\t')
    key =ss[0]
    val =ss[1]

    print "%s\t%s" % (key,val)