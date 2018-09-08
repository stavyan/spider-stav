# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/895420372/profile']

    def start_requests(self):
        cookies = "anonymid=jlsv47xk4pi7ne; depovince=GW; jebecookies=9da787f6-7f2c-4454-a3ce-26e078d4fcea|||||; _r01_=1; ick_login=02cdc71c-3d35-4822-9a1a-22d2487be8d3; Hm_lvt_cdce8cda34e84469b1c8015204129522=1536376869; Hm_lpvt_cdce8cda34e84469b1c8015204129522=1536377069; _de=6033FC0051A9A31AEF88514B9B7F4F43; p=91383938585956f057004ac3e729c0ec2; first_login_flag=1; ln_uact=15083980039; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=a0e9b0e72df3ab59c850aa7ec417cb932; societyguester=a0e9b0e72df3ab59c850aa7ec417cb932; id=895420372; xnsid=48ca46af; ver=7.0; loginfrom=null; JSESSIONID=abc761gRCNt5ggKGBn3ww; wp_fold=0; Hm_lvt_cdce8cda34e84469b1c8015204129522=1536376869; Hm_lpvt_cdce8cda34e84469b1c8015204129522=1536377325"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall(("严淑刚"), response.body.decode()))
        yield scrapy.Request(
            url='http://www.renren.com/895420372/profile?v=info_timeline',
            callback=self.parse,
        )

    def parse_detail(self, response):
        print(re.findall(("严淑刚"), response.body.decode()))

