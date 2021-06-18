# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SciencedataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    acc_number = scrapy.Field()   # 受理编号
    identifier = scrapy.Field()   # 项目编号
    pro_leader = scrapy.Field()   # 项目负责人
    business_type = scrapy.Field()  # 业务类型
    under_unit = scrapy.Field()  # 承担单位
    entry_name = scrapy.Field()  # 项目名称
    release_num = scrapy.Field()  # 下达文号
    project_year = scrapy.Field()  # 立项年度
    pass
