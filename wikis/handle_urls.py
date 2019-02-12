def set_start_urls(prefix, category):
    start_urls = []
    for cat in category:
        start_url = f'{prefix}/Category:{cat}'
        start_urls.append(start_url)
    return start_urls


def get_url(item_id, url_list):
    if item_id <= len(url_list):
        url = url_list[item_id - 1]
        item_id += 1
        return url
    else:
        return False
