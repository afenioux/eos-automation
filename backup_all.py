#!/usr/bin/env python
# +-------------------------+
# |    v0.1 by Afenioux     |
# | ./backup_all.py <usrnm> |
# | tested with python 2.7  |
# +-------------------------+

from pprint import pprint
import yaml
import getpass
import sys
from jsonrpclib import Server

login = sys.argv[1]
pwd=getpass.getpass("passwd:")


f=open('sw_list.yml')
devices=yaml.load(f.read())
f.close()

for host in devices:
	print("\n - - - - - -\n Proceeding with device : "+host)
	switch = Server( "http://{}:{}@{}/command-api".format(login, pwd, host))

	response = switch.runCmds( 1, [ "show version" ], 'json' ) 
	print "Model and version are: {} - {}".format( response[0][ "modelName" ],response[0][ "version" ])

	response = switch.runCmds( 1, ["show running-config"], 'text')
	f=open("../config/{}.txt".format(host),'w')
	f.write(response[0]['output'])
	f.close()

