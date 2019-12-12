#!/usr/bin/env python
# +-------------------------+
# |    v0.2 by Afenioux     |
# | ./deploy.py <username>  |
# | tested with python 2.7  |
# +-------------------------+

from pprint import pprint
import yaml
import getpass
import sys
import time
import re
from jsonrpclib import Server

#
# used deploy the eos.conf configuration on equipement listed in sw_list.yml
# eos.conf should be a "static" file, no template in this example
#

login = sys.argv[1]
pwd=getpass.getpass("passwd:")
sname = raw_input("Type configuration session name: ")
commands = ['configure session '+sname]

with open('eos.conf') as f:
  for line in f:
    line = line.strip()
    # this removes empty lines
    if not line:
        continue
    # do not push comments
    if re.match(r"(\s*!)", line):
        continue
    commands.append(line)
  commands.append('show session-config diffs')
#print(commands)
#sys.exit()

f=open('sw_list.yml')
devices=yaml.load(f.read())
f.close()

for host in devices:
	print("\n - - - - - -\n Proceeding with device : "+host)
	#time.sleep(2)
	switch = Server( "http://{}:{}@{}/command-api".format(login, pwd, host))

	response = switch.runCmds( 1, [ "show version" ], 'json' ) 
	print("Model and version are: {} - {}\n".format(response[0][ "modelName" ],response[0][ "version" ]))

	response = switch.runCmds( 1, commands, 'text')
	print(response[-1]['output'])

	commit = raw_input("Commit? (y/N) ")
	if commit in ["y", "Y", "Yes", "yes"]:
		print("Committing session {}".format(sname))
		response = switch.runCmds( 1, ["configure session {} commit".format(sname), 'write'], 'text')
	else:
		print("Rollback: aborting session {}".format(sname))
		response = switch.runCmds( 1, ["configure session {} abort".format(sname)], 'text')
		print("Exiting...")
		sys.exit()
	print("done.")
print("all done!")

