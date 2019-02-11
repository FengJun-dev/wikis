def xpath_handler(response, obj_xpath):
    obj = response.xpath(obj_xpath).extract()
    if len(obj) > 1:
        return obj
    return obj[0]
