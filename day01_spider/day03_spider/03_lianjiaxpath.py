
import requests,time,random
from lxml import etree
from fake_useragent import UserAgent

class LianjiaSpider:
    def __init__(self):
        self.url ="https://tj.lianjia.com/ershoufang/pg{}/"
        self.i = 0

    def get_html(self,url):
        headers ={'User-Agent':UserAgent().random}
        html = requests.get(url=url,headers=headers).text
        self.parse_html(html)

    def parse_html(self,html):
        p = etree.HTML(html)

        li_list = p.xpath('//ul[@class="sellListContent"]/li')
        item={}
        for li in li_list:

            name_list = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            item['name'] = name_list[0].strip() if name_list else None
            add_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item['address'] = add_list[0].strip() if add_list else None

            house_li =li.xpath('.//div[@class="houseInfo"]/text()')
            if house_li:
                house_li = house_li[0].split('|')
                if len(house_li) ==7:
                    item['model'] = house_li[0].strip()
                    item['area']=house_li[1].strip()
                    item['direct']=house_li[2].strip()
                    item['perfect']=house_li[3].strip()
                    item['floor']=house_li[4].strip()
                    item['year']=house_li[5].strip()
                    item['type']=house_li[6].strip()
                else:
                    item['model']=item['area']=item['direct']=item['perfect']=item['floor']=item['year']=item['type'] = None

            else:
                item['model'] = item['area'] = item['direct'] = item['perfect'] = item['floor'] = item['year'] = item['type'] = None

                total_list =li.xpath('.//div[@class="totalPrice"]/span/text()')
                item['total'] = total_list[0].strip()if total_list else None
                unit_list = li.xpath('.//div[@class="unitPrice"]/span/text()')
                item['unit'] = unit_list[0].strip() if unit_list else  None
                print(item)

                self.i +=1

    def run(self):

        for pg in range(1,101):
            url = self.url.format(pg)
            self.get_html(url=url)
            time.sleep(random.randint(1,2))
        print('number:',self.i)


if __name__ == '__main__':

    spider = LianjiaSpider()
    spider.run()






