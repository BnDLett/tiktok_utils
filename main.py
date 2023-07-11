import requests, datetime

class TiktokUtils:
    class Video:
        '''
        A TikTok video
        '''
        url         = None
        short_url   = None
        id          = None
        upload_time = None

        def __init__(self, url) -> None:
            if TiktokUtils.is_short_url(url): self.short_url = url
            # TODO: Get short URL even if it is not initially provided.

            self.url         = TiktokUtils.ensure_full_url(url)
            self.id          = TiktokUtils.get_id(self.url)
            self.upload_time = TiktokUtils.get_time(self.url)

    def get_id(full_url: str) -> int:
        '''
        "url" has be a full URL, not the short URL. 
        '''

        data       = full_url.split('/')
        partial_id = data[-1] # partial_id is the "7252031033367956742?_r=1&_t=8dkjXJ3rFvu part of the url"
        id         = partial_id.split("?")[0] # removing everything after "?" to get actual id

        return int(id)

    def get_full_url(short_url: str) -> str:
        '''
        Gets the full URL from the short URL. 
        "short_url" should be a short URL, not the full URL.
        '''
        r = requests.get(short_url)

        headers  = r.history[0].headers # Gets the long URL from a redirect
        location = headers['location']

        return location

    def is_short_url(url: str) -> bool:
        if 36 >= len(url):
            return True
        return False
    
    def ensure_full_url(url: str) -> str:
        if TiktokUtils.is_short_url(url):
            full_url = TiktokUtils.get_full_url(url)
            return full_url
        return url

    def get_time(url: str) -> datetime.datetime:
        if TiktokUtils.is_short_url(url):
            url = TiktokUtils.get_full_url(url)

        id        = TiktokUtils.get_id(url)
        binary    = bin(id)
        binary_32 = binary[0:33]                               # Going to 33 to account for "0b"
        unix_time = int(binary_32, 2)
        date_time = datetime.datetime.fromtimestamp(unix_time)

        return date_time

if __name__ == "__main__":
    tiktok_video = TiktokUtils.Video("https://www.tiktok.com/t/ZT8eKsbgF/")

    for data in tiktok_video.__dict__: print(f"{data}: {tiktok_video.__dict__[data]}")
