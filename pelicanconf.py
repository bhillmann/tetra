#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Benjamin Hillmann'
SITENAME = "Ben of 1"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_PATHS = ('articles',)

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
MARKUP = ('md',)

PLUGIN_PATHS = ('plugins', )
PLUGINS = ('ipynb.liquid', 'i18n_subsites', 'tipue_search',)

#include the search template
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

#banner
BANNER ='images/mountain_night.jpg'

#path config
STATIC_PATHS = ('images', 
    os.path.join('extra', 'favicon.ico'), 
    os.path.join('extra', 'robots.txt'), 
    os.path.join('extra', 'custom.css'),
    os.path.join('extra', 'custom.js'),)


# custom CSS
CUSTOM_CSS = 'static/custom.css'

# custom JS
CUSTOM_JS = 'static/custom.js'

THEME = 'theme/tetra-bootstrap'
PYGMENTS_STYLE = 'xcode'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/custom.js': {'path': 'static/custom.js'},
}

BOOTSTRAP_FLUID = True

# test