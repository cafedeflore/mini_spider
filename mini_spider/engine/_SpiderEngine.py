# coding=utf-8
# __author__ = cafedeflore

class _SpiderEngine():

    url_list_file = "/"
    output_directory = "/"
    max_depth = 1
    crawl_interval = 1
    crawl_timeout = 10
    target_url = ".*\.(gif|png|jpg|bmp)$"
    thread_count = 1

    def __init__(self):
        return

    def set_config(self, url_list_file, output_directory, max_depth, crawl_interval,
                   crawl_timeout, target_url, thread_count):
        self.url_list_file = url_list_file
        self.output_directory = output_directory
        self.max_depth = max_depth
        self.crawl_interval = crawl_interval
        self.crawl_timeout = crawl_timeout
        self.target_url = target_url
        self.thread_count = thread_count

    def config_tostring(self):
        to_string = str(self.url_list_file) + str(self.output_directory) + str(self.max_depth) +\
              str(self.crawl_interval) + str(self.crawl_timeout) + str(self.target_url) + str(self.thread_count)
        print to_string
        return to_string