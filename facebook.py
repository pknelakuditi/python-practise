import facebook

token = 'CAAJR8vlj2UgBADtK8TTyZAFmPZBqmfP15anAJzciMdDZAYq3leByY9Sfw5Yps8WLMPso4l0TylPUeWjCL5vRl38N97sBAi25xlBQFceoL1LGGBrZBQlRL3mRgVVq0bm4Vg1gApPwjBuaQhEKdrNTV3CcLnCZBZAxGNuQQgh2FyMvjIlQixztcUlH7Wn1QTOHAZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

friend_list = [friend['name'] for friend in friends['data']]

print len(friend_list)

print friend_list[:10]

print "------------------------------------------------------------------:"

print dir(facebook)

print facebook.__doc__
