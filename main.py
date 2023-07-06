import requests, datetime

class tiktok_utils:
    def get_id(full_url: str) -> int:
        '''
        "url" has be a full URL, not the short URL. 
        '''
        data = full_url.split('/')
        partial_id = data[-1] # partial_id is the "7252031033367956742?_r=1&_t=8dkjXJ3rFvu part of the url"

        id = partial_id.split("?")[0] # removing everything after "?" to get actual id
        return int(id)

    def get_full_url(short_url: str) -> str:
        '''
        Gets the full URL from the short URL. 
        "short_url" should be a short URL, not the full URL.
        '''
        r = requests.get(short_url)
        headers = r.history[0].headers # Gets the long URL from a redirect
        location = headers['location']

        return location

    def get_time(url: str) -> datetime.datetime:
        if 36 >= len(url):
            url = tiktok_utils.get_full_url(url) # Converting it to a full URL if needed

        id = tiktok_utils.get_id(url)
        binary = bin(id)
        binary_32 = binary[0:33] # Going to 33 to account for "0b"

        unix_time = int(binary_32, 2)
        date_time = datetime.datetime.fromtimestamp(unix_time)
        return date_time

if __name__ == "__main__":
    time = tiktok_utils.get_time("https://www.tiktok.com/t/ZT8eKsbgF/")

    print(time)
