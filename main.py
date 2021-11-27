import tweepy
import time
import os
import urllib.request
import sys

# ユーザー設定（自由に変更して下さい）
# TwitterAPI トークン
API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# いいねを監視するアカウント(公開アカウント、非公開ならFF状態にある事が必須)
# ID(screen_name)の形式で入力 例: target_user = "t0pi_"
target_user = ""

# 画像を保存するディレクトリ(初期設定は直下mediaフォルダ)
# ディレクトリが存在しない・書き込み権限が無いとエラーになります
save_path = "./media"

# TwitterAPIにアクセスするインターバル
# 最短13秒、それ以下はAPIの制限に抵触するのでおすすめしません
interval = 15

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

if os.path.exists(save_path) == False:
    print("保存対象のディレクトリが存在しません。",save_path)
    sys.exit()

time.sleep(3)

while(True):
    favorites = api.get_favorites(screen_name=target_user, count=200)
    for status in favorites:
        print(time.strftime('%Y/%m/%d %H:%M:%S'), ":", len(favorites))
        if "media" in status.entities:
            for media in status.entities["media"]:
                if os.path.exists(save_path+"/"+media['id_str']+".png") == False:
                    print("@",status.user.screen_name," > ",media['media_url'],"(",status.id,")")
                    urllib.request.urlretrieve(media['media_url'], save_path+"/"+media['id_str']+".png")
    time.sleep(interval)
    