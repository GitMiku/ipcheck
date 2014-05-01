#!/usr/bin/env python
import urllib2
import sys
def getIP(URL):
        try:
                IP=urllib2.urlopen(URL).read()
                print("Success on " + URL)
                print(IP)
                sys.exit(0)
        except urllib2.URLError:
                print("Failed on " + URL)
                return

if __name__ == '__main__':
        getIP("http://curlmyip.com")
        getIP("http://ip.telize.com/")
        getIP("http://tnx.nl/ip")
        getIP("http://myip.dnsomatic.com/")
        getIP("http://ident.me/")
        getIP("http://ifconifg.me/ip")
        getIP("http://whatismyip.akamai.com/")
        getIP("http://icanhazip.com/")

