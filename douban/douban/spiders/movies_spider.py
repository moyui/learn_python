import scrapy
from .movies_items import DoubanMoviesItem

class MoviesSpider(scrapy.Spider):
    name = 'douban_movies_top250'

    def start_requests(self):
        urls = ['https://movie.douban.com/top250']
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        item = DoubanMoviesItem()
        for movie in response.css('div.grid_view'):
            item['ranking'] = movie.css('div.pic em::text').extract_first(),
            item['movie_name'] = movie.css('span  .title::text').extract_first(),
            item['movie_board'] = movie.css('div.bd p::text').extract_first(),
            item['score'] = movie.css('div.star span.rating_num::text').extract_first(),
            item['score_num'] = movie.css('div.star span::text').extract()[3]
            yield item