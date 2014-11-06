#!/usr/bin/env python

'''Load the latest update for a Twitter user and leave it in an XHTML fragment

https://dev.twitter.com/rest/public/rate-limiting
    + Search will be rate limited at 180 queries per 15 minute window for the time being
    + 15 requests per rate limit window, then it allows you to make 15 requests per window per leveraged access token.
'''

__author__ = 'jacquelinehfl@gmail.com'

import codecs
import getopt
import sys
import twitter
import urllib
import time

TEMPLATE = """
<div class="twitter">
  <span class="twitter-user"><a href="http://twitter.com/%s">Twitter</a>: </span>
  <span class="twitter-location">%s</span>
  <span class="twitter-text">%s</span>
  <span class="twitter-relative-created-at"><a href="http://twitter.com/%s/statuses/%s">Posted %s</a></span>
</div>
"""

BOSTON_WOEID = 2367105
AL_WOEID = 2347559
MGM_CO_WOEID = 12587537
MGM_WOEID = 2453369
MGM_GEO = (32.3668052, -86.2999689, '100mi')
WYOMING_WOEID = 2347609
MISSISSIPPI_WOEID = 2347583
MISSISSIPPI_GEO = (32.585072, -89.873741, '100mi')
                                                                                    
# Currently in use                                                                  
WOEID = MISSISSIPPI_WOEID
GEO = MGM_GEO
#GEO = MISSISSIPPI_GEO

# KEYS
CONSUMER_KEY = 'CONSUER KEY'
CONSUMER_SECRET = 'CONSUMER SECRET'
ACCESS_KEY = 'ACCESS KEY'
ACCESS_SECRET = 'ACCESS SECRET'

keywords_all = [
    "Gone",
    "Ain't",
    "Don't",
    "Hell",
    "Nobody",
    "Damn",
    "Shit",
    "Mad",
    "Tired",
    "Can't",
    "Hurt",
    "Never",
    "Wait",
    "Annoying",
    "Not",
    "Weak",
    "War"
]

keywords_test = [
    "Gone",
    "Ain't",
    "Don't",
]

keywords_one = [
    "Weak"
]
keywords = keywords_one


def getNavBar():
  NAV_TEMPLATE = """
     <li>
     <a href="#%s">%s</a>
     </li>
    """

  navstring = ""
  for w in keywords:
    navstring += NAV_TEMPLATE % (w.replace("'", ""), w)
        
  Save(navstring, "nav_output")

def getSearch(keyword):
  assert keyword
  api = twitter.Api(consumer_key=CONSUMER_KEY,
              consumer_secret=CONSUMER_SECRET,
              access_token_key=ACCESS_KEY,
              access_token_secret=ACCESS_SECRET)

  # Montgomery geocode search
  statuses = api.GetSearch(term=keyword, geocode=(32.3668052, -86.2999689, '100mi'), count=50)

  # Get Twitter embedded html
  index = 1
  oembed = ""
  testoembed = ""
  results = False
  for s in statuses:
    results = False
    try:
      testoembed = api.GetStatusOembed(id=s.id, omit_script=True)['html']
      results = True
    except twitter.TwitterError, t:
      print t
      print "keyword %s @ index %d failed" % (keyword, index)
      # sleep for 16 minutes, twitter has a fifteen minute timeout
      # and a 180 max search for 15 minutes
      d = t[0][0]
      # If Rate limit exceeded is true then wait
      if (d['code'] == 88):
        print "Sleeping... "
        time.sleep(960)
      ## break

    if results:
      oembed += "<h3>#%d</h3>\n" % index
      oembed += testoembed 
      oembed += "\n\n"
      index +=1

  return oembed

def buildSearchPage():
  PAGE_TEMPLATE="""
  <div id="%s">
  <h2>%s</h2>
  %s
  </div>
  """
  pagestring = ""
  pagenum = 1
  for w in keywords:
    pagestring += PAGE_TEMPLATE % ( w.replace("'", ""), w, getSearch(w))
    page_output = "page_output_%d" % (pagenum)
    Save(pagestring, page_output)
    pagestring = ""
    pagenum += 1
        
def Save(xhtml, output):
  out = codecs.open(output, mode='w', encoding='ascii',
                    errors='xmlcharrefreplace')
  out.write(xhtml)
  out.close()

def main():
  getNavBar()
  buildSearchPage()

if __name__ == "__main__":
  main()
