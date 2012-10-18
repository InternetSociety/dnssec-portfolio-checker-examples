This repository contains some examples of scripts using the REST interface to the
"DNSSEC Portfolio Checker" from SIDN Labs.  This free service from SIDN Labs lets
you easily check the DNSSEC status of a large number of domains.

A web interface where you can upload a CSV file of domain names is available at:

http://check.sidnlabs.nl:8080/form

That page also contains the list of status messages and also information about the
REST interface.  To use the REST interface, you simply query:

    http://check.sidnlabs.nl:8080/check/<domainname>

as in:

    http://check.sidnlabs.nl:8080/check/internetsociety.org

If you have access to the '''curl''' command, you could issue a command such as:

    curl http://check.sidnlabs.nl:8080/check/internetsociety.org

The programs found in this repository are simple examples of how you could use the
interface.  They were written purely because I wanted to experiment with the API
from SIDN Labs and thought I would share my examples.

More examples are welcome if you would like to contribute additional ways to use it
or code in other languages.

These examples are licensed under a permissive MIT-style license. Feel free to use
them in any way you wish. (See the LICENSE file for the full text.)

The "Portfolio Checker" itself is a program written in GO and available from SIDN Labs at:

https://github.com/SIDN/unboundcheck

Thanks to SIDN Labs for making this service available for free to the public.

Have fun!

- Dan York, Internet Society, york@isoc.org

