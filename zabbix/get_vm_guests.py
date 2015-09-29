#!/usr/bin/env python

import re

# Open file and remove as much junk as possible on first pass (spaces, "running", "idle")
# File is output of running "virsh list" from cron

try:
    f = open('/var/log/zabbix/vm_guests.txt')
    virsh_list = [re.sub(' ', '', line).strip('\n').strip('running').strip('idle').strip('no state') for line in f if line != ""]

    # Remove guest number
    guest_list = [re.sub("^[0-9]+","", line) for line in virsh_list]

    # Last pass to clean up the output
    output = [x.split(' ') for x in guest_list if x.endswith(".com")]
    vm_str = ''
    if len(output) > 0:
        for item in output:
            vm_str +=  ' '.join(item) + " "
    else:
        vm_str = "None"

    print vm_str

except IOError:
    print "ERROR: No vm guest file on host!"
