def show_magicians(magicians):
    for magician in magicians:
        print(magician.title() + ".")


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "Greate " + magicians[i]

        

magicians_names = ['david', 'agonisyan', 'blane']
magicians_names_copy = ['david', 'agonisyan', 'blane']

show_magicians(magicians_names)
make_great(magicians_names_copy)
show_magicians(magicians_names)
show_magicians(magicians_names_copy)
