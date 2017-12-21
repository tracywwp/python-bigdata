#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午4:34
# @Author  : tracy
# @Site    : 
# @File    : map.py
# @Software: IntelliJ IDEA

#缓存 实现白名单 统计word

import os
import sys
import gzip


def getFileHandler(f):
    fileIn=open(f)
    return fileIn

def getCacheFileHandlers(f):
    fileHandlersList=[]
    if os.path.isdir(f):
       for fd in os.listdir(f):
           fileHandlersList.append(getFileHandler(f+'/'+fd))
    return fileHandlersList

def read_local_file_func(f):
    wordSet= set()
    for cacheFile in getCacheFileHandlers(f):
        for line in cacheFile:
            word=line.strip()
            wordSet.add(word)
    return wordSet

#读取白名单 map操作
def mapper_func(whiht_list):
    wordSet = read_local_file_func(whiht_list)

    for line in sys.stdin:
        ss=line.strip().split(' ')
        for s in ss:
            word=s.strip()
            if word!= "" and (word in wordSet):
                print "%s\t%s" % (s,1)

if __name__ == "__main__":
    module = sys.modules[__name__]
    func = getattr(module, sys.argv[1])
    args = None
    if len(sys.argv) > 1:
        args = sys.argv[2:]
    func(*args)