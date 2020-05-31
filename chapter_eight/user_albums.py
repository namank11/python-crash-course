"""
 Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
 Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
 Be sure to include a quit value in the while loop.
"""


def make_albums(artist, album):
    albums = {}
    albums[artist] = album
    return albums


albums = {}
message = ''
while (message != 'quit'):
    message = input("Would you like to add another?")
    if (message == 'quit'):
        print("bye!")
    else:
        artist = input("Enter Artist Name")
        album = input("Enter Album Name")
        albums.update(make_albums(artist, album))
print(albums)
