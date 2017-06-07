#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'sourcepirate'
SITENAME = u'PeerWorld'
SITEURL = 'http://peerworld.in'
SITESUBTITLE = 'Knowledge is free'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DISQUS_SITENAME = u'peerworld'

THEME = 'themes/cleanblog'
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/sourcepirate'),
          ('github', 'https://github.com/sourcepirate'),
          ('facebook','https://facebook.com/sathya.shadow'),
          ('envelope','mailto:sathya@peerworld.in'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
