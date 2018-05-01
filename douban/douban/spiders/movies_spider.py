import scrapy
import time

from .movies_items import DoubanMoviesItem

class MoviesSpider(scrapy.Spider):
    name = 'douban_movies_top250'

    def start_requests(self):
        urls = ['https://movie.douban.com/top250']
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        item = DoubanMoviesItem()
        for movie in response.css('ol.grid_view li'):
            item['ranking'] = movie.css('div.pic em::text').extract_first(),
            item['movie_name'] = movie.css('div.hd span.title::text').extract_first(),
            item['movie_board'] = '%s%s' % ( movie.css('div.bd p::text').extract()[0], movie.css('div.bd p::text').extract()[1])
            item['score'] = movie.css('div.star span.rating_num::text').extract_first(),
            item['score_num'] = movie.css('div.star span')[3].css('span::text').extract_first()
            yield item
        next_url = response.css('div.paginator span.next a::attr(href)') .extract_first()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url
            time.sleep(5)
            yield scrapy.Request(next_url, callback=self.parse)