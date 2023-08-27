import requests
import random
import tweepy
import time

# Add your API key, API secret key, Access token, and Access token secret
consumer_key = "ENTER_YOUR_CONSUMER_KEY"
consumer_secret = "ENTER_YOUR_CONSUMER_SECRET"
access_token = "ENTER_YOUR_ACCESS_TOKEN"
access_token_secret = "ENTER_YOUR_ACCESS_TOKEN_SECRET"

# =========Authenticate to Twitter===========
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Set the time interval in seconds between each tweet/retweet
interval = 21600


likehashtags = ["#lovequotes", "#quoteoftheday", "#motivation", "#selfhelp", "#writer", "LifeIsBeautiful","solitude", "authors", "#Readers", "psychology"]

while True:
    # Collect quotes from API
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    data = response.json()
    number_of_hashtags = 2
    hashtags = ["#quotes", "#inspiration", "#motivation", "#positivity", "#quoteoftheday","#quotestolive", "#inspirationalquotes", "#motivationalquotes", "#dailyquotes", "#quotesdaily", "#positivevibes", "#mindfulness", "#goodvibes", "#wordsofwisdom", "#DailyMotivation","#lifequotes", "#InspritionalQuotes", "#InspiringQuotes", "#MotivationalWords", "#BestLine", "#WordsOfLife", "#Author", "#BestQuotes", "#AspiringYouth", "#QuotesForYou", "#LostIntoMotivation", "#TrandingQuotes", "#Happiness","#life", "#Vibes" ]
    selected_hashtags = random.sample(hashtags, number_of_hashtags)
    quote = data['content'] + " - " + data['author'] + "\n" + " ".join(selected_hashtags)

    try:
        # Auto-tweet the collected quote
        tweet = api.update_status(quote)
        print("Tweet sent successfully:", tweet.text)
    except tweepy.TweepError as error:
        print("Error sending tweet:", error)
        continue
    # To like the tweets in a several hashtag
# Randomly select a hashtag to search for tweets
    likeselected_hashtag = random.choice(likehashtags)
    likehashtag_tweets = tweepy.Cursor(api.search_tweets, q=likeselected_hashtag).items(2)



    for tweet in likehashtag_tweets:
        try:
            # Auto-like the tweet
            api.create_favorite(tweet.id)
            print("Tweet liked successfully:", tweet.text)
        except tweepy.error.TweepError as error:
            print("Error liking tweet:", error)
            continue

        # Wait for some time before searching for new tweets again
    time.sleep(interval) # sleep for 60 seconds