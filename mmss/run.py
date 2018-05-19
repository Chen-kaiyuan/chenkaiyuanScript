# -*- coding:utf-8 -*-

import ConfigParser
import sys
import os

def Realtime(comm):
    # read conf setting
    cf = ConfigParser.ConfigParser()
    cf.read('./mmmssconfig.conf')
    # read conf key-value
    configname = cf.sections()
    for i in range(len(configname)):
        confproject = configname[i]
        keynames = cf.options(confproject)
        for b in range(len(keynames)):
            value = cf.get(confproject, keynames[b])
            if comm == 'start':
                os.system('sh start.sh {0} {1} {2}'.format(confproject, keynames[b], value))
            elif comm == 'stop':
                os.system('sh stop.sh {0} {1} {2}'.format(confproject, keynames[b], value))
            else:
                print('ERROR: Not data with config')

def history():
    # read conf setting
    cf = ConfigParser.ConfigParser()
    cf.read('./mmmssconfig.conf')
    # read conf key-value
    configname = cf.sections()
    for i in range(len(configname)):
        confproject = configname[i]
        keynames = cf.options(confproject)
        for b in range(len(keynames)):
            value = cf.get(confproject, keynames[b])
            if comm == 'start':
                os.system('sh catdata.sh {0} {1} {2}'.format(confproject, keynames[b], value))
            else:
                print('ERROR: Not data with config')


if __name__ == '__main__':
    table = sys.argv[1]
    comm = sys.argv[2]
    if table == '0':
        Realtime(comm)
    elif table == '1':
        history(comm)
    else:
        print('error: no the table!')