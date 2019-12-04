import scrapy
import json
import find_interest_ids

class Snap_spider(scrapy.Spider):
    name = "snap"
    start_urls = [
        'https://snapshot.numerator.com/brand/2k_games',
    ]

    def parse(self, response):
        for snap in response.css('body'):
            yield{
                'name' : snap.css('div.content div.title_block div.title_left div.title::text').get(),
                'interest_id': find_interest_ids.remote('name'),
                'values': snap.css('div.block_content_top div.block_charts table.block_charts tr.block_charts_row td.block_charts_col_right::text').getall(),                
            }
