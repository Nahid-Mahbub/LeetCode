class Codec:

    def __init__(self):
        self.map = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        shortUrl = "http://tinyurl.com/" + str(self.id)
        self.map[shortUrl] = longUrl
        self.id += 1
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.map[shortUrl]


codec = Codec()

url = "https://leetcode.com/problems/design-tinyurl"

tiny = codec.encode(url)
print(tiny)

original = codec.decode(tiny)
print(original)