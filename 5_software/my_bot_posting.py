from twitter import *
import time

my_bot = Twitter(auth=OAuth(
    '1977499933-cu6wXh7X48AV7rRrF4LhlruI3El9p4nQUSZbKLv',
    'VkhC0axbwEInxSbesq0qduj1oS9ZAO4tzuLqZohmn7SiL',
    'IeuGaViCctVJ6rIKxbYfSiXzm',
    '7pIbwODvhQ58YYycHvUEi6MfNNMffju3mQHRDjGqFR6yrrvc2g'
))

my_tweets = ["Covid isn't real", "Teach yourself #PsyOps", "Drain the Swamp"]

# # this index is going to be our counter to go through all our tweets
index = 0

# # we have a loop that will count until it reaches the total number
# # of tweets in the `my_tweets` list (line 20)
while index < len(my_tweets):
    print("posting...")                     # we print something to see that we're actually posting
    my_bot.statuses.update(status=my_tweets[index])     # this is the line that posts the tweet
    index += 1                              # then we increase the counter to move on to the next tweet
    time.sleep(5)                          # and finally we tell the program to wait for 30 seconds
