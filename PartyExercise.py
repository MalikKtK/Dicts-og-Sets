# Define two sets, one for invited friends and one for RSVP'd friends
invited_friends = {'Malik', 'Jens', 'Niels', 'Haci', 'Mark'}
rsvp_friends = {'Malik', 'Haci', 'Patrick', 'Peter'}

# Names of friends who have not RSVP'd
not_rsvped = invited_friends - rsvp_friends
print("Friends who have not RSVP'd:", not_rsvped)

# Names of friends who were not invited but RSVP'd
not_invited_but_rsvped = rsvp_friends - invited_friends
print("Friends who were not invited but RSVP'd:", not_invited_but_rsvped)

# Names of friends who are common in both lists (i.e., invited and RSVP'd)
common_friends = invited_friends & rsvp_friends
print("Common friends who are invited and RSVP'd:", common_friends)
