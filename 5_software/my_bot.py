from twitter import *

# this part allows you to authenticate your bot to twitter
# to obtain your credentials, go to developer.twitter.com,
# create a new app and generate keys and tokens
my_bot = Twitter(auth=OAuth(
    '1977499933-cu6wXh7X48AV7rRrF4LhlruI3El9p4nQUSZbKLv',
    'VkhC0axbwEInxSbesq0qduj1oS9ZAO4tzuLqZohmn7SiL',
    'IeuGaViCctVJ6rIKxbYfSiXzm',
    '7pIbwODvhQ58YYycHvUEi6MfNNMffju3mQHRDjGqFR6yrrvc2g'
))

# this line just prints the name of the account
# associated with the keys you've
# name = my_bot.VerifyCredentials().name
# print("Hello, " + name)

# this where you would specify your search term
# more information on searching here: https://python-twitter.readthedocs.io/en/latest/searching.html
# and how twitter expects your query to be composed: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
search_term = "#Brexit"
results = my_bot.GetSearch(term=search_term)

# you can also find tweets per user timeline:
# screen_name = "THE USER HANDLE HERE"
# results = my_bot.GetUserTimeline(screen_name=screen_name, count=200)

print(results)

# this line opens a new file called 'tweets.txt'
# and we will append our results to it
file = open("tweets.txt", "a+")

for result in results:
    print("=============")
    print("raw result: ")
    print(result)
    print("=============")
    print("tweet: "+result.text)
    print("name: "+result.user.name)

    # here we save each of our result in the file
    file.write(result)

# finally, we close the file, now that we're done with it
f.close()
