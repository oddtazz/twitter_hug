__author__ = 'gaurav'

import random
from twitter import *
config = {}
execfile("config.py", config)
twitter = Twitter(
		auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

# My username
username = "oddtazz"

# Getting my friends list
query = twitter.friends.ids(screen_name = username)

# Getting twitter ids of my friends
friends = query["ids"]
friends_int = len(friends)

# Getting a random friend from my friends list
friends_to_hug_int = random.randrange(0, friends_int)
friends_to_hug = query["ids"][friends_to_hug_int]

# Qurying twitter to get the username
subquery = twitter.users.lookup(user_id = friends_to_hug)
person = subquery[0]["screen_name"]

# Creating a status
new_status = "@"+person+" *Hugs* :D #RandomHugOfTheDay "

# Tweeting the random hug for the day
results = twitter.statuses.update(status = new_status)
print "updated status: %s" % new_status