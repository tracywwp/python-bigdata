#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午3:29
# @Author  : tracy
# @Site    : 
# @File    : red_sort.py
# @Software: IntelliJ IDEA

import sys

baseValue=10000

for line in sys.stdin:
    key,val=line.strip().split('\t')
    print str(int(key)-baseValue) + "\t" +val
