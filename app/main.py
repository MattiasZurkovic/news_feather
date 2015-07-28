__author__ = 'mattias'

from flask import Flask
from flask import render_template
import feedparser
import urllib, collections, hmac, binascii, time, random, string
from hashlib import sha1

app = Flask(__name__)


# The index method and page will show the TOP(most popular) news stories from all the sources(i.e. CNN, Forbes, BBC, etc.)
@app.route('/')
def index():
    TOP_URLS = ['http://www.forbes.com/feeds/popstories.xml',     ##### Forbes - Most Popoular
                'http://rss.cnn.com/rss/edition.rss',             ##### CNN - Most Popular
                'http://feeds.wired.com/wired/index',             ##### Wired - Most Popular
                'http://www.cbc.ca/cmlink/rss-world',             ##### CBC - Most Popular (World News)
                'http://rss.nytimes.com/services/xml/rss/nyt/InternationalHome.xml', ##### NY Times - World News
                ]

    entries = []
    for url in TOP_URLS:
        entries.extend(feedparser.parse(url).entries)

    all_entries_sorted = sorted(entries, key=lambda e: e.published_parsed, reverse=True)

    return render_template('index.html', entries=all_entries_sorted)


@app.route('/tech')
def tech_page():
    TECH_URLS = ['http://feeds.feedburner.com/TechCrunch/',
                 'http://www.wired.com/category/gear/feed/',
                 'http://rss.cnn.com/rss/edition_technology.rss',
                 'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml'
                 ]

    entries = []
    for url in TECH_URLS:
        entries.extend(feedparser.parse(url).entries)

    all_entries_sorted = sorted(entries, key=lambda e: e.published_parsed, reverse=True)

    return render_template('tech.html', entries=all_entries_sorted)

@app.route('/politics')
def politics_page():
    POL_URLS = ['https://www.realwire.com/rss/?id=467&row=&view=Synopsis',
                'http://feeds.reuters.com/Reuters/PoliticsNews',

                ]

    entries = []
    for url in POL_URLS:
        entries.extend(feedparser.parse(url).entries)

    all_entries_sorted = sorted(entries, key=lambda e: e.published_parsed, reverse=True)

    return render_template('politics.html', entries=all_entries_sorted)


if __name__ == '__main__':
    app.run()