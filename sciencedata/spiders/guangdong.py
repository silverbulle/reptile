import scrapy
from sciencedata.items import SciencedataItem


class QuotesSpider(scrapy.Spider):
    name = "guangdong"

    def start_requests(self):
        urls = [
            'http://sjfb.gdstc.gd.gov.cn/app/sjkf/kjxm_101003.jsp'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):  # 开始正式爬虫后会默认调用的处理函数

        post_data = {
            'draw': '1',
            'start': '0',
            'length': '30',
            'selectType': '01',
        }
        # FormRequest发送POST请求
        yield scrapy.FormRequest(
            "http://sjfb.gdstc.gd.gov.cn/app/sjkf/kjxm_101003.jsp",
            formdata=post_data,
            callback=self.after_login
        )

        page = response.url.split("/")[-2]

        filename = 'guangdong-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
