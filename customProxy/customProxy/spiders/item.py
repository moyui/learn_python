# -*- coding: utf-8 -*-
import scrapy

class CustomProxyItem(scrapy.Item):
    proxy_address = scrapy.Field() #代理地址
    proxy_port = scrapy.Field() #代理端口
    proxy_type = scrapy.Field() #代理类型