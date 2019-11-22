import scrapy
import json

class Snap_spider(scrapy.Spider):
    name = "snap"
    start_urls = [
        'https://snapshot.numerator.com/brand/2k_games',
        'https://snapshot.numerator.com/brand/sony',
        'https://snapshot.numerator.com/brand/microsoft',
        'https://snapshot.numerator.com/brand/bayer',
    ]

    def parse(self, response):
        for snap in response.css('body'):
            yield{
                'name' : snap.css('div.content div.title_block div.title_left div.title::text').get(),
                'values': snap.css('div.block_content_top div.block_charts table.block_charts tr.block_charts_row td.block_charts_col_right::text').getall().trim(),
            }
        
            