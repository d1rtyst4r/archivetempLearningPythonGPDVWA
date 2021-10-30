# Task 8-7
def make_album(artist, album_title, number_of_tracks=''):
    if number_of_tracks:
        album = {'artist': artist, 'album title': album_title, 'number of track': number_of_tracks}
    else:
        album = {'artist': artist, 'album title': album_title}
    return album


miasma = make_album('the black dahlia murder', 'miasma', 15)
steal_this_album = make_album('system of a down', 'steal this album')
slipknot = make_album('slipknot', 'slipknot')

print(miasma)
print(steal_this_album)
print(slipknot)

# Task 8-8
while True:
    print("\n Please enter artist name and album!")
    print("enter 'q' to quit at any time")

    a_name = input("Please enter artist: ")
    if a_name == 'q':
        break
    a_title = input("Please enter album title: ")
    if a_title == 'q':
        break
    album = make_album(a_name, a_title)
    print(album)
