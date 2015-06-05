# -*- coding:utf-8 -*-
# !/usr/bin/env python
################################################################################
#
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
This module is the mutil thread class for mini_spider
"""

import threading

class SpiderThread(threading.Thread):
    def __init__(self, queue, timeout, ):
        threading.Thread.__init__(self)


    def run(self):
        base_path = "D:\\test\\forpython\\"
        file = base_path + self.name + ".txt"
        # file = base_path + "test" + ".txt"
        print file
        f = open(file, 'a')
        while len(data) > 0:
            if lock.acquire():
                s = data[0:10]
                del data[0:10]
                lock.release()
                # print s
                if s is None:
                    break
                for i in s:
                    a = src.check.Solution()
                    a.work(i, f)
                    f.flush()