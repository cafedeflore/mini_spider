__author__ = 'cafedeflore'
#coding=utf-8

import getopt
import sys

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
            print "帮助信息：没有帮助^_^"
            sys.exit()
        elif o == "-c":
            print a
        else:
            assert False, "unhandled option"

main()
print "hello world!"