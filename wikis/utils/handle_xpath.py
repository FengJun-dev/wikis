def xpath_handler(response, item_xpath):
    obj = response.xpath(item_xpath).extract()
    if len(obj) > 1:
        return obj
    return obj[0]
