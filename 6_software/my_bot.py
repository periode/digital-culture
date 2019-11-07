import twitter

my_bot = twitter.Api(
    consumer_key='1Fez3DePMTDs0o0IFgdRM0KRu',
    consumer_secret='aeVgKyOAEHYAX0hFpRAZiOwAEqIE7RSGRgpxdY2uZ2S6g8BWRN',
    access_token_key='1192073673102053377-JQLTZGfwL3ZvKndpn0FKv9J7ybPGQy',
    access_token_secret='CIn7cSVFRtOp20TI7k8LoUvO519d9qFlmubOshtd1P9kx'
  )

name = my_bot.VerifyCredentials().name
print("Hello, " + name)

search_term = "#MeToo"
results = my_bot.GetSearch(term=search_term)

for result in results:
    print(result.text)
    print("----------")
