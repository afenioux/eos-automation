# Arista EOS Automation

Theses are some basic scripts I use for automation.
The username should be provide in agument while the password will be requested by the prompt


## sw_list.yml
the list of switches/routers you want to connect to

## backup_all.py 
```
./backup_all.py <username>
passwd:

 - - - - - -
 Proceeding with device : router1
Model and version are: DCS-7280SR-48C6-F - 4.20.8M-INT

 - - - - - -
 Proceeding with device : router2
Model and version are: DCS-7280SR2A-48YC6-F - 4.20.8M-INT
```

## cli_run.py 
```
./cli_run.py <username>
passwd:
Type your full command (eg: 'show running-config | include ecmp'): show running-config | include bgp
 Proceeding with device : router1
Model and version are: DCS-7280SR-48C6-F - 4.20.8M-INT
router bgp 65535
   no bgp default ipv4-unicast
   no bgp additional-paths receive
   no bgp bestpath as-path multipath-relax

 - - - - - -
 Proceeding with device : router2
Model and version are: DCS-7280SR2A-48YC6-F - 4.20.8M-INT
``` 

## deploy.py
If you chose to no commit a change, the script will rollback configuration and exit without processing next device.

eos.conf : the commands you want to deploy with deploy.py

```
./deploy.py <username>
passwd:
Type configuration session name: bgp

 - - - - - -
 Proceeding with device : router1
Model and version are: DCS-7280SR-48C6-F - 4.20.8M-INT

--- system:/running-config
+++ session:/bgp-session-config
@@ -824,7 +824,6 @@
    neighbor BPG-IBGP peer-group
    neighbor BPG-IBGP remote-as 65536
    neighbor BPG-IBGP update-source Loopback0
+   neighbor BPG-IBGP additional-paths receive
-   neighbor BPG-IBGP additional-paths send

Commit? (y/N) N
Rollback: aborting session bgp
Exiting...
```
