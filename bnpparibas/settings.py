BOT_NAME = 'bnpparibas'

SPIDER_MODULES = ['bnpparibas.spiders']
NEWSPIDER_MODULE = 'bnpparibas.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'bnpparibas.pipelines.BnpparibasPipeline': 100,

}