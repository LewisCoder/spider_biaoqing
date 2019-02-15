
BOT_NAME = 'biaoqing'

SPIDER_MODULES = ['biaoqing.spiders']
NEWSPIDER_MODULE = 'biaoqing.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

IMAGES_STORE = '/home/lewis/test/biaoqing2'

DOWNLOAD_DELAY = 0.5

SPIDER_MIDDLEWARES = {
   'biaoqing.middlewares.UserAgentMiddlewares': 100,
}

ITEM_PIPELINES = {
   'biaoqing.pipelines.BiaoqingPipeline': 1,
}
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]

