# -*- coding: utf-8 -*-
import scrapy
from aliexpresscoupons.items import AliexpressItem


class CouponsSpider(scrapy.Spider):
    name = "coupons"
    allowed_domains = ["coupon.aliexpress.com"]
    start_urls = (
        'http://coupon.aliexpress.com/proengine/sellerCouponList.htm',
    )

    def parse(self, response):
        for li in response.xpath('//ul[@class="coupon-list clearfix"]/li'):
            item = AliexpressItem()
            item['url'] = li.xpath('a/@href').extract()[0]
            item['couponPrice'] = float(li.xpath('a/div/span[@class="coupon-price"]/em/text()').extract()[0].strip().replace('$', ''))
            item['couponPriceText'] = ''.join(li.xpath('a/div/span[@class="coupon-price"]/descendant-or-self::*/text()').extract())
            item['couponOrderPrice'] = float(li.xpath('a/div/span[@class="coupon-order-price"]/em/text()').extract()[0].strip().replace('$', ''))
            item['couponOrderPriceText'] = ''.join(li.xpath('a/div/span[@class="coupon-order-price"]/descendant-or-self::*/text()').extract())
            yield item
        page = response.xpath('//a[@class="page-next"]/@page').extract()
        if len(page) == 1:
            page = page[0]
            data = {
                'page': page,
                '_csrf_token_': response.xpath('//input[@name="_csrf_token_"]/@value').extract()[0],
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip,deflate',
                'Accept-Language': 'en-US,en;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
            }
            yield scrapy.FormRequest('http://coupon.aliexpress.com/proengine/sellerCouponList.htm',
                                     formdata=data,
                                     headers=headers,
                                     callback=self.parse)