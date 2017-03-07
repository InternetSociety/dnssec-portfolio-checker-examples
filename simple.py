#!/usr/bin/env python
#
# A simple example of using the SIDN Labs DNSSEC Portfolio Checker at http://portfolio.sidnlabs.nl/form
# via the REST API
#

import urllib2

portfolio = ['internetsociety.org','ietf.org','sidnlabs.nl','google.com','www.dnssec-failed.org']

for domain in portfolio:
    status = urllib2.urlopen('http://portfolio.sidnlabs.nl/check/%s' % domain).read().split(',')[2]
    print "%s - %s" % (status, domain)

#
# Regarding what is going on in the first line of the for loop, the result sent back from
# the Portfolio Checker has this format:
#
# internetsociety.org,"",secure,"" 
#
# The "urllib2.urlopen().read()" retrieves that information.
# ".split(',')" breaks the result into a list based on the comma
# "[2]" references the third item in the list (because python lists start at 0)
#
