from scrapy.loader.processors import MapCompose, TakeFirst

wiki_processor_type = {
    "input_processor": MapCompose(),
    "output_processor": TakeFirst(),
}
