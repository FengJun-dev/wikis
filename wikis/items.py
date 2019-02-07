import scrapy

from scrapy.loader.processors import MapCompose, TakeFirst


class WikisItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst(),
    )
    content = scrapy.Field(
        input_processor=MapCompose(),
    )
    comment = scrapy.Field(
        input_processor=MapCompose(),
    )
    page = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst(),
    )
    main_category = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst(),
    )
    category = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst(),
    )
    en_category = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst(),
    )
    book = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst(),
    )
    sub_category = scrapy.Field(
        output_processor=TakeFirst(),
    )
    article_id = scrapy.Field(
        output_processor=TakeFirst(),
    )
    quality = scrapy.Field(
        output_processor=TakeFirst(),
    )
