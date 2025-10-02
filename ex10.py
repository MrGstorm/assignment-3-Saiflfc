###############################################################################
#  Program Name   : ex10.py
#  Author         : saif elmebayad
#  Task           : his program asks for 3 friends' names and prints them all.
###############################################################################


friends = []

for _ in range(3):
    name = input("Enter a friend's name: ")
    friends.append(name)

print("Your friends are:")
for friend in friends:
    print(friend)

