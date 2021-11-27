# app-python-twitter-liketosave
![gif](https://github.com/topi-k/app-python-twitter-liketosave/blob/main/images/top.gif)

## Overview
Twitterで指定したアカウントがいいねしたツイートの画像を自動的に保存するプログラムです。  
This is a program that automatically saves images of tweets liked by a specified account on Twitter.  

## Requirement
Python 3.9.x / tweepy が利用できる環境であれば、オペレーティングシステム問わずどこでも動作します。  
It will run on any operating system, as long as Python 3.9.x and tweepy are available.  

確認環境
- Windows 11 Pro (Build:22000.318)
- Python 3.9.7
- tweepy 4.4.0
- urllib3 1.26.7
 
 ## Usage
 1. Twitter Developer Platform (developer.twitter.com) からアプリを作成し、トークンを取得する。   
 Create an app and obtain a token from the Twitter Developer Platform (developer.twitter.com).  
 2. 取得したトークンをmain.pyの9から12行目に記述する。  
 Write the obtained token in lines 9 to 12 of main.py.  
 3. いいねを監視するアカウントと画像を保存するディレクトリを、main.pyの20と24行目に記述する。  
 Write the account to monitor for likes and the directory to store the images in lines 20 and 24 of main.py.  
 4. 実行する。  
 Run it.
 
 ## Features
 対象のアカウントによっていいねされたツイートを、最新のツイート順に200件取得します。  
 取得されたツイートの中で画像が添付されており、かつ保存されていない画像があった場合、保存を実行します。  
 
 画像は _Twitter画像ID + ".png"_ の形式で保存されます。  
 保存された画像が移動・削除されたり、名前が変更されると（再度取得が可能な場合のみ）再取得されます。
 
 最新のツイートから取得するという仕様上、古すぎるツイートの画像は取得されない場合があります。    
 
 Get 200 tweets liked by the target account, ordered by the latest tweet.
 If the got tweet has an image attached and not yet saved, it will be saved.
 
 The image will be saved in the format _Twitter Image ID + ".png"_.
 If a saved image is moved, deleted, or renamed (only if it can be retrieved again), it will be retrieved again.

 Due to the specification of retrieving images from the most recent tweets, images from tweets that are too old may not be retrieved.  
 
 **保存された画像の著作権は、著作者に帰属します。**  
 **The copyright of the saved images belongs to the author.**
 
 ## Reference
 Tweepy/tweepy (https://github.com/tweepy)
 
 ## Author
 [Twitter](https://twitter.com/t0pi_)
 
 ## Licence
 MIT
