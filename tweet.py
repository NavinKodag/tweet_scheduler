import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("XXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXX")
auth.set_access_token("XXXXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

# Create API object
api = tweepy.API(auth)
#set localtimezone if running on a server
os.environ["TZ"] = "Asia/Kolkata"
time.tzset()
counter=1
while counter!=421:
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    time.sleep(60)
    if current_time=='04:19':
        api.update_status(f'''its 420 \n.\n.\n.\n.\n.\n{counter}/420''')
        print("it's 420 ")
        counter=counter+1
    else:
        print(current_time)
        pass
