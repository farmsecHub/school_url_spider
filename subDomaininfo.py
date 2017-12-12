#/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys

subdomains_brute_path = '/opt/six/subDomainsBrute'
sublist3r_path = '/opt/six/Sublist3r'
subdomain3_path = '/opt/six/subdomain3/'

suDomaininfo_path = '/opt/subDomainsinfo.txt'

def sublist3r(domain):

    os.chdir(sublist3r_path)
    command = 'python sublist3r.py -d %s -v -o %s' % (domain,subdomain3_path)
    os.system(command)


def subdomains_brute(domain):

    os.chdir(subdomains_brute_path)
    command = 'python subDomainsBrute.py %s -i ' % domain
    os.system(command)

def split_domains(domain):

    os.chdir(subdomains_brute_path)
    command = "cat %s.txt|sort -d|uniq|awk '{print ($1)}' >> %s" % (domain,subdomain3_path)
    os.system(command)


def subdomain3(domain):

    os.chdir(subdomain3_path)
    command = 'python brutedns.py -d %s -s hight' % domain
    os.system(command)

def main():

    try:
        domain = sys.argv[1]

    except IndexError:
        print "please enter domain as python subDomaininfo.py baidu.com"

    else:
        subdomains_brute(domain)
        split_domains(domain)
        sublist3r(domain)

if __name__ == "__main__":

    main()



