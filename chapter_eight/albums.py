"""
 Write a function called make_album() that builds a dictionary describing a music album.
 The function should take in an artist name and an album title,
 and it should return a dictionary containing these two pieces of information.
 Use the function to make three dictionaries representing different albums.
 Print each return value to show that the dictionaries are storing the album information correctly.
 Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
 If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
 Make at least one new function call that includes the number of songs on an album.
"""


def make_album(artist_name, album_title, number_of_songs=None):
    return {artist_name: {album_title: number_of_songs}}

albums={}

for i in range(0, 3):
    artist_name = input("Enter the name of the artist")
    album_title = input("Enter the name of the album")
    number_of_songs = input("Enter the number of songs in album or press enter")
    if number_of_songs:
        albums.update(make_album(artist_name, album_title, number_of_songs))
    else:
        albums.update(make_album(artist_name, album_title, number_of_songs))

print(albums)
