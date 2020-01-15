#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import sys, getopt, os
import uuid


def usage():
    usage_info = '''STBC means Synchronize Table Between Cluster initials of words
It can be parallel sync data and ddl to destination cluster
    
Usage:
    STBC <--OPTIONS>
    
OPTIONS:
    --dest_dbname        destination cluster database name
    --dest_hostname      destination cluster host name
    --dest_dbuser        destination cluster database user used
    --dest_port          destination cluster database port, default be 5432
    --src_dbname         source database name
    --src_hostname       source database host name
    --src_dbuser         source database user name used
    --src_port           source database port, default be 5432
    --inclusive_schema   can be mutiple specify
    --exclusive_schema   can be mutiple specify
    --inclusive_table    can be mutiple specify
    --exclusive_table    can be mutiple specify
    --parameter-file     command line parameter in the file
    --drop               drop destination table before transfer
    --truncate           truncate destination table before transfer
    --delete             delete destination table before transfer
    --where              if you use --table-file parameter ,you can specify this option : schema.table;where date > 20190101
    --analyze            after data transfered ,analyze destination cluster table
    --encoding           UTF8 or GB18030, default be UTF8
    --force              force recreate destination cluster table, if Inconsistent table structure
    --incremental        incremental sync table data to the destination cluster
    --jobs               concurrency thread
    --verbose            print very verbosity running log
    --version            show this utility version
    --help               dispaly help information
    -?                   display help information, similar to the --help
    
Example: 
    STBC --dbname <database name> --hostname <host name> --username <user name>
    STBC --dbname my_dbname --hostname mdw001 --username gpadmin --port 5432
    STBC --parameter-file STBC.conf --incremental
    '''
    print usage_info
    sys.exit(0)

def parseArgs(argv):
    dbname   = ''
    hostname = ''
    dbuser   = ''
    port     = ''
    inclusive_schema = ''
    exclusive_schema = ''
    inclusive_table  = ''
    exclusive_table  = ''
    force            = ''
    incremental      = ''
    jobs             = ''
    try:
        opts, args = getopt.getopt(argv,
                                   "?d:h:U:s::S::t::T::p:Fi:j:P::",
                                   ["help", "dbname=", "hostname=", "username=","port=",
                                    "inclusive_schema=","exclusive_schema","inclusive_table","exclusive_table",
                                    "force","incremental","jobs="]
                                   )
        for opt, arg in opts:
            print arg
            if opt in ('--help', '-?'):
                usage()
            elif opt in ("-d", "--dbname"):
                dbname = arg
            elif opt in ("-U", "--username"):
                dbuser = arg
            elif opt in ("-h", "--hostname"):
                hostname = arg
            elif opt in ("-p","--port"):
                port = arg
            else:
                usage()
    except getopt.GetoptError as err:
        print err


parseArgs(sys.argv[1:])

# 拼写sql
sql = "PGDATABASE= PGPORT=5432 PGCLIENTENCODING=gb18030 PGUSER=gpadmin "
sql += ""

cmds = """ssh gpadmin@10.9.10.130 -q << EOF
 psql -tAXc 'select * from pg_class limit 10'
 EOF
"""
# os.system(cmds)


# get uuid code
# print str(uuid.uuid4()).replace('-','')
