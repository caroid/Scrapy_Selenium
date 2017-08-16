import scrapy
from selenium import webdriver
from Scrapy_Selenium.items import ScrapySeleniumItem
import logging
logging.basicConfig(level=logging.INFO)


class SeleniumScrapySpider(scrapy.Spider):

    name = 'selenium'
    allowed_domains = 'roadrunnersports.com'
    start_urls = ['http://www.roadrunnersports.com/rrs/products/14948/mens-nike-air-zoom-pegasus-34/?cc=007',]

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        items1 = []
        self.driver.get("http://www.roadrunnersports.com/rrs/products/14948/mens-nike-air-zoom-pegasus-34/?cc=007")

        # color
        color_tags = self.driver.find_elements_by_class_name("ref2QIColor ")
        for ctag in color_tags:
            item = ScrapySeleniumItem()
            ctag.click()
            col = self.driver.find_element_by_id("ref2QIColorTitle").text
            item['color'] = col

            # get sizes
            size_width_list = []
            size_tags = self.driver.find_elements_by_class_name("ref2QISize ")
            for stag in size_tags:
                stag.click()
                str_size = stag.get_attribute("name")

                # get width
                width_tags = self.driver.find_elements_by_class_name("ref2QIWidth")
                for wtag in width_tags:
                    wtag.click()
                    width = wtag.get_attribute("name")
                    atag = self.driver.find_element_by_id("ref2QIInventoryTitleS")
                    size_width_list.append(str_size,width,atag.text)
            item['size_widht_list'] = size_width_list
            items1.append(item)
        # self.driver.close()
        self.driver.quit()
        return items1
