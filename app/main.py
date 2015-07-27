__author__ = 'mattias'

from flask import Flask
from flask import render_template
import feedparser
import urllib, collections, hmac, binascii, time, random, string
from hashlib import sha1

app = Flask(__name__)


# URLs
# 'http://www.forbes.com/real-time/feed2/'         ##### Forbes - Lastest Headlines
#



# The index method and page will show the TOP(most popular) news stories from all the sources(i.e. CNN, Forbes, BBC, etc.)
@app.route('/')
def index():
    TOP_URLS = ['http://www.forbes.com/feeds/popstories.xml',     ##### Forbes - Most Popoular
                'http://rss.cnn.com/rss/edition.rss',             ##### CNN - Most Popular

                ]

    ##### Valve Feed
    entries = []
    for url in TOP_URLS:
        entries.extend(feedparser.parse(url).entries)

    all_entries_sorted = sorted(entries, key=lambda e: e.published_parsed, reverse=True)

    return render_template('index.html', entries=all_entries_sorted)


if __name__ == '__main__':
    app.run()