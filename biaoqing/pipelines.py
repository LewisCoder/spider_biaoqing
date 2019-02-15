import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
class BiaoqingPipeline(ImagesPipeline):
    # 重构三个方法
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['url'], meta={'title': item['title'], 'page': item['page']})

    def item_completed(self, results, item, info):
        # if not results[0][0]:
        #     raise DropItem('下载失败')
        print(results)
        return item

    def file_path(self, request, response=None, info=None):
        # 拆分文件名
        title = request.meta['title'] + '.' + 'jpg'
        page = request.meta['page']
        filename = u'{0}/{1}'.format(page, title)
        return filename
