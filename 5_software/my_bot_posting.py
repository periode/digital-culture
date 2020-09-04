import twitter
import time

# this part allows you to authenticate your bot to twitter
# to obtain your credentials, go to developer.twitter.com,
# create a new app and generate keys and tokens
my_bot = twitter.Api(
    consumer_key='YOUR CONSUMER KEY HERE',
    consumer_secret='YOUR SECRET CONSUMER KEY HERE',
    access_token_key='YOUR TOKEN HERE',
    access_token_secret='YOUR SECRET TOKEN HERE'
  )

# this line just prints the name of the account
# associated with the keys you've
name = my_bot.VerifyCredentials().name
print("Hello, " + name)

# here we specify an array of text that we want to be tweeted
my_tweets = ["Poutou2022", "LamissAzab2027", "JeremyDumont2032"]

# this index is going to be our counter to go through all our tweets
index = 0

# we have a loop that will count until it reaches the total number
# of tweets in the `my_tweets` list (line 20)
while index < len(my_tweets):
    print("posting...")                     # we print something to see that we're actually posting
    my_bot.PostUpdate(my_tweets[index])     # this is the line that posts the tweet
    index += 1                              # then we increase the counter to move on to the next tweet
    time.sleep(30)                          # and finally we tell the program to wait for 30 seconds
