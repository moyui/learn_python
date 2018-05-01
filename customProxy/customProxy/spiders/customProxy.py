import scrapy
import requests  
import time
from .item import CustomProxyItem

class CustomProxy(scrapy.Spider):
    name = 'xicispider'
    urls = []
    user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    
    for i in range(1,9):
        url = r'http://www.xicidaili.com/nn/%s' % str(i)
        urls.append(url)

    def start_requests(self):
        headers = {'User-Agent': self.user_agent}
        for url in self.urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)
    
    def parse(self, response):
        item = CustomProxyItem()
        all_list = response.css('table#ip_list tr')
        for i in range(1, len(all_list)):
            address = all_list[i].css('td::text').extract()[0]
            port = all_list[i].css('td::text').extract()[1]
            types = all_list[i].css('td::text').extract()[5]

            if self.filter(address, port, types) == False:
                continue

            item['proxy_address'] = address
            item['proxy_port'] = port
            item['proxy_type'] = types

            yield item

    def filter(self, address, port, types):
        if types == 'HTTP':
            return False #proxy = {'http': 'http://%s:%s' % (address, port)}
        elif types == 'HTTPS':
            proxy = {'https': 'http://%s:%s' % (address, port)}
        else:
            return False

        try:
            if requests.get('https://movie.douban.com/top250', proxies=proxy, timeout=0.5).status_code == 200:
                return True
            else:
                return False
        except:
            return False