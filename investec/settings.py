BOT_NAME = 'investec'

SPIDER_MODULES = ['investec.spiders']
NEWSPIDER_MODULE = 'investec.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'investec.pipelines.InvestecPipeline': 100,

}