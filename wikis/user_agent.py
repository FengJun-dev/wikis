from fake_useragent import UserAgent


class WikiRandomUserAgentMiddleware(object):
    def __init__(self, crawler):
        super(WikiRandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent(verify_ssl=False)
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)

        user_agent_random = get_ua()
        request.headers.setdefault('User-Agent', user_agent_random)
