#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andrew Lane'
SITENAME = u'anti-social science'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# static files
STATIC_PATHS = [
    'slides',
    'slides/css/theme',
    'slides/lib/css',
    'slides/lib/js',
    'slides/js',
    'slides/plugin/markdown',
    'slides/plugin/highlight',
    'slides/plugin/notes',
    ]

EXTRA_PATH_METADATA = {
    'slides/css/theme/night.css': {'path': 'slides/css/theme/night.css'},

    'slides/js/reveal.js': {'path': 'slides/js/reveal.js'},
    
    'slides/lib/css/zenburn.css': {'path': 'slides/lib/css/zenburn.css'},
    'slides/lib/js/head.min.js': {'path': 'slides/lib/js/head.min.js'},
    'slides/lib/js/classList.js': {'path': 'slides/lib/js/classList.js'},

    'slides/plugin/markdown/marked.js': {'path':
    'slides/plugin/markdown/marked.js'},
    

    'slides/plugin/markdown/markdown.js': {'path':
    'slides/plugin/markdown/markdown.js'},

    'slides/plugin/highlight/highlight.js': {'path':
    'slides/plugin/highlight/highlight.js'},

    'slides/plugin/notes/notes.js': {'path':
    'slides/plugin/notes/notes.js'},

    'slides/earth-modelling.html': {'path': 'slides/earth-modelling.html'}
    
    }
