import tweepy
 
# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "1703060209340694528-rpE1QiU0JdoZA8sMi2vmWoqYsKyqCQ"
consumer_secret = "4V42WocpLxbMcE4QbSJsJoiQwYBfDe1z0AgJH317BiGuF"
access_key = "BH1LoWR807u29Uy68eoMk3EBe"
access_secret = "xRuN3CXbvJvHyFl0maQ4ZAvlhEx8MIwfMtwW8EuA9Iea0dpm5s"
 
# Function to extract tweets
def get_tweets(username):
        global consumer_key
        global consumer_secret
        global access_key
        global access_secret
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuth2AppHandler(consumer_key, consumer_secret)
 
        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)
 
        # Calling api
        api = tweepy.API(auth)
 
        # 200 tweets to be extracted
        number_of_tweets=200
        tweets = api.user_timeline(screen_name="@keboola")
 
        # Empty Array
        tmp=[]
 
        # create array of tweet information: username,
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
        for j in tweets_for_csv:
 
            # Appending tweets to the empty array tmp
            tmp.append(j)
 
        # Printing the tweets
        print(tmp)
 
 
# Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("twitter-handle")