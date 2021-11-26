import tweepy
import time
import os
import urllib.request

# ユーザー設定（自由に変更して下さい）
API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
User = "" # 取得対象アカウント（公開アカウントのみ）
# ここまで

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

while(True):
    favorites = api.get_favorites(count=200)
    # printing the screen names of the status posters
    for status in favorites:
        print(time.strftime('%Y/%m/%d %H:%M:%S'), ":", len(favorites))
        print(status.id)
        if "media" in status.entities:
            for media in status.entities["media"]:
                if os.path.exists("./media/"+media['id_str']+".png") == False:
                    print(status.user.screen_name," > ",media['media_url'],"(",status.id,")")
                    urllib.request.urlretrieve(media['media_url'], "./media/"+media['id_str']+".png")
    time.sleep(15)
