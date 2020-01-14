#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import sys, getopt, os
import uuid

def parseArgs(argv):
    dbname   = ''
    hostname = ''
    dbuser   = ''
    try:
        opts,args= getopt.getopt(argv,"?:h:d:U:h",["help","dbname","hostname","username"])
        for opt, arg in opts:
            print arg
            if opt in ('-h','--help','-?'):
                print 'STBC --dbname <database name> --hostname <hostname> --username <username>'
                sys.exit()
            elif opt in ("-d", "--dbname"):
                dbname = arg
            elif opt in ("-U", "--username"):
                dbuser = arg
            elif opt in ("-h","--hostname"):
                hostname = arg
    except getopt.GetoptError as err:
        print err


parseArgs(sys.argv[1:])

#拼写sql
sql  = "PGDATABASE= PGPORT=5432 PGCLIENTENCODING=gb18030 PGUSER=gpadmin "
sql += ""

cmds = """ssh gpadmin@10.9.10.130 -q << EOF
 psql -tAXc 'select * from pg_class limit 10'
 EOF
"""
#os.system(cmds)



#get uuid code
#print str(uuid.uuid4()).replace('-','')
