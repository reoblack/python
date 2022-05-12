from icrawler.builtin import *

crawler = BingImageCrawler(storage={"root_dir": './bad'})
crawler.crawl(keyword='dog',max_num=500)