#coding=utf-8

import getopt
import sys
import ConfigParser
import engine._SpiderEngine as _SpiderEngine


def version():
    print "version 1.0.0"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vhc:")
    except getopt.GetoptError as err:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)
    for o, a in opts:
        if o == "-v":
            version()
            sys.exit()
        elif o == "-h":
            # spider_engine = _SpiderEngine._SpiderEngine()
            # spider_engine.config_tostring()
            # spider_engine.set_config()
            print "帮助信息：没有帮助^_^"
            sys.exit()
        elif o == "-c":
            # print a
            cf = ConfigParser.ConfigParser()
            cf.read(a)
            spider_engine = _SpiderEngine._SpiderEngine()
            try:
                spider_engine.set_config(cf.get("spider", "url_list_file"), cf.get("spider", "output_directory"),
                                     cf.getint("spider", "max_depth"), cf.getint("spider", "crawl_interval"),
                                     cf.getint("spider", "crawl_timeout"), cf.get("spider", "target_url"),
                                     cf.getint("spider", "thread_count"))
            except:
                raise Exception("配置文件出错")
                sys.exit(2)
            spider_engine.config_tostring()

            # print a
        else:
            assert False, "unhandled option"

main()
# print "hello world!"