__author__ = 'mattias'

from flask import Flask
from flask import render_template
import feedparser
import urllib, collections, hmac, binascii, time, random, string
from hashlib import sha1

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/valve')
def valve():
    ##### RSS Feed Urls:
    VALVE_URLS = ['http://store.steampowered.com/feeds/news.xml'     # Steam URL
                  'http://blog.counter-strike.net/index.php/feed/',  # CSGO URL
                  'http://blog.dota2.com/feed/',                     # DOTA URL
                  'http://www.teamfortress.com/rss.xml',             # TF2 URL
                  'http://www.sourcefilmmaker.com/rss.xml'           # Source Film Maker URL
                  ]

    ##### Valve Feed
    valve_entries = []
    for url in VALVE_URLS:
        valve_entries.extend(feedparser.parse(url).entries)

    valve_entries_sorted_reverse = sorted(valve_entries, key=lambda e: e.published_parsed, reverse=True)
    valve_entries_sorted_oldest = sorted(valve_entries, key=lambda e: e.published_parsed, reverse=False)

    return render_template('valve.html', entries=valve_entries_sorted_reverse, reg_entries=valve_entries_sorted_oldest)


@app.route('/test_feed')
def test_feed():
    return render_template('test.html', csgo_html = csgo_link_parse())


def csgo_link_parse():
    csgo_url = feedparser.parse('http://blog.counter-strike.net/index.php/feed/')
    for post in csgo_url.entries:
        return post.title

if __name__ == '__main__':
    app.run()