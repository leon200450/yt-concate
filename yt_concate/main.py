import urllib.request
import json
from yt_concate.settings import api_key
from dotenv import load_dotenv
import dotenv

CHANNEL_ID = 'UC5PYHgAzJ1wLEidB58SK6Xw'


def get_all_video_in_channel(channel_id):

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links


#print(get_all_video_in_channel(CHANNEL_ID),len(get_all_video_in_channel(CHANNEL_ID)) )
print(api_key)
