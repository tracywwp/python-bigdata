#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 上午11:15
# @Author  : tracy
# @Site    : 
# @File    : red.py
# @Software: IntelliJ IDEA


#reduce过程 统计字数的个数
import sys

currentWord=None

countPool=[]

sum=0

for line in sys.stdin:
    word,val=line.strip().split('\t')

    if currentWord == None:
        currentWord=word

    if currentWord !=word:
       for count in countPool:
           sum+=count
       print "%s\t%s" % (currentWord,sum)
       currentWord =word
       countPool=[]
       sum=0

    countPool.append(int(val))

