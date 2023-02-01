import scrapy
import re
import pandas as pd
import json
import js2xml
from scrapy import Request
from tutorial.items import FilmographyItem


url_actor = 'https://raw.githubusercontent.com/AugusteDebroise/IMDB/main/TOP_200_1990_2020_ACTOR'
actor = pd.read_csv(url_actor)

##actor = pd.read_csv('/Users/augustedebroise/PycharmProjects/IMDB_scrapper/Scrapper/TOP_200_1990_2020_ACTOR')
actor.drop_duplicates(subset='1', keep=False, inplace=True)
actor = actor.reset_index(drop=True)
url = actor["1"].tolist()
url_full = []
for single_url in url:
    single_url_clean =  re.findall(r'(/name/\w+)', single_url)
    single_url_clean = single_url_clean[0]
    url_full.append(f'https://www.imdb.com{single_url_clean}/fullcredits/')
#print(url_full)
print(len(url_full))

global end
begin, end = 0, 15
url_partial = url_full[begin:end]

global my_list_full
my_list_full = {}

from scraper_api import ScraperAPIClient
client = ScraperAPIClient('5ca78c48aa8acbdb986749993fb56c3b')

class Spider_Actor_General_Info(scrapy.Spider):
    name = "Actor_filmography"

    def start_requests(self):
        start_urls = url_partial
        for url in start_urls:
            yield scrapy.Request(client.scrapyGet(url=url, country_code='us'), callback=self.parse)

    def parse(self,response):

        item = FilmographyItem()
        base_url_raw = response.request.url
        base_url = re.findall(r'(%2Fname%2Fnm\w+)', base_url_raw)
        base_url = base_url[0]
        base_url = base_url.replace("%2F", "/")

        my_dict = {}

        self.actor = response.xpath('//div[@class="parent"]//h3//a/text()').get()
        self.role = response.xpath('//div[@class="head"]/@data-category').getall()
        self.entry = response.xpath('///div[@class="filmo-row even" or @class="filmo-row odd"]')
        for line in self.entry:
            self.film_title = line.xpath('.//b//a/text()').get()
            self.film_date = line.xpath('.//span[@class="year_column"]/text()').get()
            self.film_date_clean = re.sub('\n', '', re.sub('\n\xa0', '',self.film_date))
            self.film_url = line.xpath('.//b//a/@href').get()
            self.personage_and_extra_info = line.xpath('./text()').getall()
            self.personage_and_extra_info_clean = [item.strip() for item in self.personage_and_extra_info]
            self.personage_and_extra_info_clean = list(filter(None, self.personage_and_extra_info_clean))
            self.job = line.xpath('.//@id').re_first('(\w+)-tt')
            my_dict[self.film_title] = [self.job, self.film_url, self.film_date_clean, self.personage_and_extra_info_clean]


            item['actor']= self.actor
            item['film_title'] = self.film_title
            item['job'] = self.job
            item['film_url'] = self.film_url
            item['film_date'] = self.film_date_clean
            item ['personage_and_extra_info_clean']= self.personage_and_extra_info_clean
            yield item

        my_list_full[base_url] = my_dict
        print(len(my_list_full.keys()))

        #with open(f'/Users/augustedebroise/PycharmProjects/IMDB_scrapper/Scrapper/HTML_test_pages/page{REF_1}.html', 'wb') as html_file:
        #    html_file.write(response.body)

    def closed(self, spider):
        my_list_full_df = pd.DataFrame(my_list_full.items(), columns=['actor', 'filmography'])
        print(my_list_full_df)
        #my_list_full_df.to_csv(f'Actor_1990_2020_filmo_{begin}_{end}.csv', mode='a', index=True, header=True)
        print('END');
