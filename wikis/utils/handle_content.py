from wikis.utils.handle_xpath import xpath_handler


def content_handler(response):
    content_xpath = '//div[@class="poem"]/p/text()|//div[@class="poem"]/p/span/text()'
    content = xpath_handler(response, content_xpath)
    if not content:
        n_content_xpath = '//div[@class="mw-parser-output"]/div[@class="prp-pages-output"]/p/text()'
        b_content_xpath = '//div[@class="mw-parser-output"]/div[@class="prp-pages-output"]/p/span/text()'
        content_xpath = f'{n_content_xpath}|{b_content_xpath}'
        content = xpath_handler(response, content_xpath)
        return content
    return content
