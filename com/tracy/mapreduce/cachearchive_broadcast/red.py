#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午4:34
# @Author  : tracy
# @Site    : 
# @File    : red.py
# @Software: IntelliJ IDEA


import sys


def reduer_func():
    currentWord=None
    sum=0
    countPool=[]

    for line in sys.stdin:
        word,val=line.strip().split('\t')

        if(currentWord == None):
            currentWord=word

        if(currentWord!=word):
            for count in countPool:
                sum+=count
            print "%s\t%s" % (currentWord,sum)
            currentWord=word
            countPool=[]
            sum=0
        countPool.append(int(val))

    for count in countPool:
        sum += count
    print "%s\t%s" % (currentWord, str(sum))




if __name__ == "__main__":
    module = sys.modules[__name__]
    func = getattr(module, sys.argv[1])
    args = None
    if len(sys.argv) > 1:
        args = sys.argv[2:]
    func(*args)