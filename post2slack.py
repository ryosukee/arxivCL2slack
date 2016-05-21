from api import API

api = API()

c = 0
for tw in reversed(api.get_tweets()):
    c += 1
    twid = tw['id']
    text = tw['text']
    name = tw['user']['name'] + '@' + tw['user']['screen_name']
    icon_url = tw['user']['profile_image_url_https']
    tw_url_template = 'https://twitter.com/{}/status/{}'
    tw_url = tw_url_template.format(tw['user']['screen_name'], twid)
    api.post2slack(tw_url + '\n' + text, name, icon_url=icon_url)
    api.post2slack('-' * 50, '　', icon_emoji=':white:')
    api.set_last_id(twid)
