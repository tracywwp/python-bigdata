#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午4:09
# @Author  : tracy
# @Site    : 
# @File    : red_sort.py
# @Software: IntelliJ IDEA

import sys

for line in sys.stdin:
    idx_id, key, val = line.strip().split('\t')
    print '\t'.join([key, val])