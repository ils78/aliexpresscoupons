# -*- coding: utf-8 -*-

# Scrapy settings for aliexpress project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'aliexpresscoupons'

SPIDER_MODULES = ['aliexpresscoupons.spiders']
NEWSPIDER_MODULE = 'aliexpresscoupons.spiders'

COOKIES_ENABLED = True
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_DELAY = 1

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'aliexpress (+http://www.yourdomain.com)'
