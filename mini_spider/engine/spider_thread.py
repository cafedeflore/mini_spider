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

import time
import threading
import logging
import re

from engine import UrlParse
from engine import SpiderEngine

class SpiderThread(threading.Thread):
    """
    the module provider multi thread for mini spider
    """

    def __init__(self, queue, timeout, interval, file_path, max_depth, target_url, total_set):
        threading.Thread.__init__(self)
        self.queue = queue
        self.timeout = timeout
        self.interval = interval
        self.file_path = file_path
        self.max_depth = max_depth
        self.target_url = target_url
        self.total_set = total_set
        self.lock = threading.Lock()

    def need_download(self, url):
        """
        judge whether the url needs download.
        downloaded, no
        not match the rules, no
        :param url: the url
        :return: True, False
        """
        if not UrlParse.UrlParse.is_url(url):
            return False
        try:
            pattern = re.compile(self.target_url)
        except Exception as err:
            logging.error("the target url is not re..compile fail: %s" % self.target_url)
            return False
        if len(url.strip(' ')) < 1 or not pattern.match(url.strip(' ')):
            return False
        if url in self.total_set:
            return False
        return True

    def run(self):
        """
        run the thread.
        get task from queue. And add the sub url into queue. BFS.
        :return: no return
        """
        while True:
            try:
                url_leaf = self.queue.get(block=True, timeout=self.timeout)
            except Exception as err:
                logging.info("this thread can not get a task. job done.")
                break
            # print url_leaf is None
            self.queue.task_done()
            #sleep interval
            time.sleep(self.interval)

            #download the url
            if self.need_download(url_leaf.url):
                UrlParse.UrlParse.download(self.file_path, url_leaf.url)
            self.lock.acquire()
            self.total_set.add(url_leaf.url)
            self.lock.release()
            #get the sub urls from url
            sub_urls = UrlParse.UrlParse.get_urls(url_leaf.url)
            new_level = url_leaf.level + 1
            if new_level > self.max_depth:
                continue
            for url in sub_urls:
                url_leaf_temp = SpiderEngine.UrlLeaf(url, new_level)
                self.queue.put(url_leaf_temp)