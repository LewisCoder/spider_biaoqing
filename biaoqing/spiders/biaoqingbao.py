
import scrapy
from biaoqing.items import BiaoqingItem

class BiaoqingbaoSpider(scrapy.Spider):
    name = 'biaoqingbao'
    allowed_domains = ['fabiaoqing.com/biaoqing']
    start_urls = ['https://www.fabiaoqing.com/biaoqing/']

    def parse(self, response):
        divs = response.xpath('//*[@id="bqb"]/div[1]/div')
        next_url = response.xpath('//div[contains(@class,"pagination")]/a[last()-1]/@href').extract_first()
        base_url = 'https://fabiaoqing.com'
        for div in divs:
            items = BiaoqingItem()
            items['url'] = div.xpath('a/img/@data-original').extract_first()
            items['title'] = div.xpath('a/@title').extract_first()
            items['page'] = next_url.split('/')[-1]
            yield items
        if next_url:  # 如果存在下一页则进行翻页
            url = base_url + next_url  # 拼接字符串
            yield scrapy.Request(url, self.parse, dont_filter=True)
