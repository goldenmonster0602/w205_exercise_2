import tweepy

consumer_key = "9AnS4F7jaXZbjsLn3rNRnA27v";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "pRb500hZyJCXXIPraeTLm39zJXJSq0pVYY5DaGfRG4uo7sxZnc";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "4102231403-S1He7a26X9Y8n4h9IzZVYgNsKXfEmvFzy5Kroos";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "Rxpd8BURMN8ZD8wxpQ24AibFLkXa1WQOVQJxoEe6ovQLA";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



