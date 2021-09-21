class Url:
    def __init__(self, scheme=None, authority=None, path=None, query=None, fragment=None):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __str__(self):
        return f"{self.scheme}://{self.authority}/{self.path}/{self.query}/{self.fragment}"

    def __eq__(self, other):
        return str(self) == str(other)


url1 = Url('scheme', 'authority', 'path', 'query', 'fragment')
url2 = Url('scheme', 'authority', 'path', 'query', 'fragment')
url3 = Url('scheme1', 'authority2', 'path3', 'query4', 'fragment5')
print(url1 is str)
print(url1 == url3)
print(url1 == url2)


class HttpsUrl(Url):
    def __init__(self, scheme='https', authority=None, path=None, query=None, fragment=None):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment


class HttpUrl(Url):
    def __init__(self, scheme='http', authority=None, path=None, query=None, fragment=None):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment


class GoogleUrl(HttpsUrl):
    def __init__(self):
        super().__init__(authority='google.com')


class WikiUrl(HttpsUrl):
    def __init__(self):
        super().__init__(authority='wikipedia.org')


print(WikiUrl())
print(GoogleUrl())
