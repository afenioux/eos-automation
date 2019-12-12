#!/usr/bin/env python
# +-------------------------+
# |    v0.1 by Afenioux     |
# | ./cli_run.py <username> |
# | tested with python 2.7  |
# +-------------------------+

from pprint import pprint
import yaml
import getpass
import sys
from jsonrpclib import Server

login = sys.argv[1]
pwd=getpass.getpass("passwd:")
command = raw_input("Type your full command (eg: 'show running-config | include ecmp'): ")
#command = 'show ip access-lists'


f=open('sw_list.yml')
devices=yaml.load(f.read())
f.close()

for host in devices:
	print("\n - - - - - -\n Proceeding with device : "+host)
	switch = Server( "http://{}:{}@{}/command-api".format(login, pwd, host))

	response = switch.runCmds( 1, [ "show version" ], 'json' ) 
	print "Model and version are: {} - {}".format( response[0][ "modelName" ],response[0][ "version" ])

	response = switch.runCmds( 1, [command], 'text')
	print response[0]['output']

