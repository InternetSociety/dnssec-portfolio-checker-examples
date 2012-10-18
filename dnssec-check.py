#!/usr/bin/env python

import sys
import urllib2

if len(sys.argv) > 1:
    for domain in sys.argv[1:]:
        results = urllib2.urlopen('http://check.sidnlabs.nl:8080/check/%s' % domain).read().split(',')
        if results[1] == 'nodata':
            print "%s - domain not found" % (domain)
        else:
            print "%s - %s" % (domain, results[2])
            
else:
    print "Usage: dnssec-check.py <domain> <domain> <domain>\n(for as many domains as you wish to check)"
