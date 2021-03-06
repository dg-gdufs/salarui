# encoding: utf-8

from urllib import parse

from crawler.spiders import BaseSpider
from crawler.items import *
from scrapy.http.request import Request
from common.url_qs import QCWY_SALARY
from config.settings_config import OFFER_NAME
from utils.format_util import FormatUtil

class QianChengWuYouSpider(BaseSpider):
    name = 'qcwy'
    # 工资、名称、页数
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,{},{},2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://search.51job.com/',
        }
    }

    def start_requests(self):
        for offer in OFFER_NAME:
            offer = parse.quote(offer)
            for salary in QCWY_SALARY:
                meta = {"salary": salary, "offer": offer, "page": 1}
                yield Request(self.url.format(salary,offer,'1'),meta=meta)

    def parse(self, response):
        js = response.json().get('engine_jds')
        if not js:
            return
        for i in js:
            try:
                item = OfferItem()
                item['offer_id'] = '0_' + i['jobid']
                item['offer'] = i['job_name']
                item['category'] = parse.unquote(response.meta['offer'])
                item['area'] = FormatUtil.qcwy_area_format(i['workarea'])
                item['salary'] = FormatUtil.qcwy_salary_format(i['providesalary_text'])
                if i['workyear']:
                    item['workyear'] = '0_' + i['workyear']
                if i['degreefrom']:
                    item['degree'] = '0_' + i['degreefrom']
                item['date'] = i['issuedate']
                yield item
            except Exception as e:
                self.send_log(2, "item出错抛弃 ==> {} ==> item:{}".format(e, item))

        response.meta['page'] += 1
        yield Request(self.url.format(response.meta['salary'],response.meta['offer'],str(response.meta['page'])),meta=response.meta)
