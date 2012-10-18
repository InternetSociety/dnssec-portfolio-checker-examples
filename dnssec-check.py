#!/usr/bin/env python
#
# A simple program that will check the DNSSEC status of multiple domains entered on
# the command line using the REST API to SIDN Labs free DNSSEC Portfolio Checker found at:
#   http://check.sidnlabs.nl:8080/form
# Information about the API can be found further down on that page
#

import sys
import urllib2

# Check that the program was called with command-line arguments and if so, check the domains

if len(sys.argv) > 1:
    for domain in sys.argv[1:]:
        results = urllib2.urlopen('http://check.sidnlabs.nl:8080/check/%s' % domain).read().split(',')

        # Check the second field in the results to see if the domain was a valid domain

        if results[1] == 'nodata':
            print "%s - domain not found" % (domain)
        else:
            print "%s - %s" % (domain, results[2])
            
else:
    print "Usage: dnssec-check.py <domain> <domain> <domain>\n(for as many domains as you wish to check)"
