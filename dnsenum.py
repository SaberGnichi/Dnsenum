import sys
import socket
import os
import argparse

def touch(path):
    os.mknod(path)

def addLine(f, l):
    with open(f, 'r') as of:
        c = of.read()
    if len(c) > 0:
        c += '\n' + l
    else:
        c += l
    with open(f, 'w') as of:
        of.write(c)

def getIP(host):
    try:
       IP = socket.gethostbyname(host)
       return IP
    except Exception:
       return False
description = 'This tool can be used to brute discover subdomains related to a specific domain based on a list of common words\n'
description += 'Url : \n'
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-d','--domain', help='the target main domain name', required=True)
parser.add_argument('-n','--name', help='the target name', required=True)
parser.add_argument('-f','--file', help='the filename that contains subs', required=True)
args = vars(parser.parse_args())
domain = args['domain']
name = args['name']
file = args['file']
if not os.path.exists('targets'):
    os.makedirs('targets')
directory = 'targets/' + name
if not os.path.exists(directory):
    os.makedirs(directory)
ips = []
hosts = []
ipsfile = 'targets/' + name + '/ips.txt'
hostsfile = 'targets/' + name + '/hosts.txt'
gfile = 'targets/' + name + '/all.txt'
touch(ipsfile)
touch(hostsfile)
touch(gfile)
with open(file, "r") as subs:
    for sub in subs:
        d = sub.strip() + '.' + domain
        ip = getIP(d)
        if ip != False:
            isnewhost = True
            j = 0
            while j < len(hosts) and isnewhost == True:
                if d == hosts[j]:
                    isnewhost = False
                j += 1
            if isnewhost == True:
                hosts.append(d)
                ips.append(ip)
                display = d + ' - ' + ip
                print display
                addLine(ipsfile, ip)
                addLine(hostsfile, d)
                addLine(gfile, display)
