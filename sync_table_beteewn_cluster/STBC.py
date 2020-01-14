#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import sys, getopt, os

def parseArgs(argv):
    inputfile = ''
    outputfile = ''
    try:
       opts,args= getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
       for opt, arg in opts:
           if opt == '-h':
               print 'commandsLineArgv -i <inputfile> -o <outputfile>'
               sys.exit()
           elif opt in ("-i", "--ifile"):
               inputfile = arg
           elif opt in ("-o", "--ofile"):
               outputfile = arg
    except getopt.GetoptError as err:
        print err

    print 'input file name is ：', inputfile
    print 'output file name is：', outputfile

#parseArgs(sys.argv[1:])

#拼写sql
sql  = "PGDATABASE=gpadmin PGPORT=5432 PGCLIENTENCODING=gb18030 PGUSER=gpadmin "
sql += ""

cmds = """ssh gpadmin@10.9.10.130 -q << EOF
 psql -tAXc 'select * from pg_class limit 10'
 EOF
"""
print os.system(cmds)




