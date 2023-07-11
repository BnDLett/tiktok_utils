# tiktok_utils
Some utility tools for TikTok, such as getting ID or getting the upload time of a video.

# Currently implemented features
1. get_id
   - Gets the ID of a URL, require a full ID (for example: `https://www.tiktok.com/@_pubblicita__/video/7133151752492174597?is_from_webapp=1&sender_device=pc&web_id=7252535274533701163`)
2. get_full_url
   - Gets the full URL of a short URL (for example: `https://www.tiktok.com/t/ZT8eKsbgF/`)
3. get_time
   - Gets the date and time a video was uploaded. Can use both short and long URL's.
4. is_short_url
   - Returns `True` if the URL is the short form of the URL, otherwise `False` if it is the full URL.
5. ensure_full_url
   - Ensures the URL is the full URL. (for example: `https://www.tiktok.com/t/ZT8eKLttq/` would go to `https://www.tiktok.com/@getrickrolled401/video/7218398016015813915?_t=8dkmDAA0lmo&_r=1`)

You are also able to create a `TiktokUtils.Video` object, which contains the upload date, full URL and id.

# Additional information
Inspired by @CKEnthusiant's video, https://www.tiktok.com/t/ZT8eKLttq/ <br>
This has not been 100% tested, so there may be issues on some videos and no issues on others. <br>
If you wish to contribute, then feel free. All help is appreciated.
