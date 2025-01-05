# coding: utf8
file_name = 'alice.txt'

try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file " + file_name + " does not exist.")
else:
    # Counting numbers of words in file
    words = contents.split()
    num_words = len(words)
    print("The file " + file_name + " has about " + str(num_words) + " words!") 