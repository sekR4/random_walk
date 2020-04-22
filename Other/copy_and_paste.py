import os

path = os.path.dirname(os.path.abspath(__file__))

with open(path + "/vengaboys_up_and_down_lyrics.txt", "r") as file:
    lyrics = file.read()

print(lyrics.lower().replace('up and down', 'copy and paste'))

# I know folks who call this a solid migration strategy. It's like your cloud
# service provider is offering you an excellent tool set, but you're only used
# to the hammer. So you try to cut flowers, paint the walls etc. with a hammer,
# since it's the best tool. Then you figure, your people are working too slowly.
# So you force all team members to use the hammer. Beat out technology with
# more manpower?
