import tweepy
from tweepy.auth import OAuthHandler
import sys
import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument("-file_path", "--Input", help = "Show Output")
parser.add_argument("-title", "--input", help = "Show Output")
parser.add_argument("-json", "--Input1", help = "Show Output")
args = parser.parse_args()
f = open(args.Input1)
data = json.load(f)
jsonData = data["Twitter"]
CONSUMER_KEY= jsonData["CONSUMER_KEY"]
CONSUMER_SECRET= jsonData["CONSUMER_SECRET"]
access_token=jsonData["Access_token"]
access_token_secret=jsonData["Access_token_secret"]
file=args.Input+jsonData["File_Name"]
def main():
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    # Upload image
    media = api.media_upload(file)
    # Post tweet with image
    tweet = args.input
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])
    print(f"Media_Id: {post_result.id_str}")
if __name__ == "__main__":
    main()