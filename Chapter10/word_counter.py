#coding: utf8

def count_words(filename : str):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #print("Sorry, the file " + filename + " does not exist.")
        pass
    else:
        # Counting numbers of words in file
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words!")

file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file_name in file_names:
    count_words(file_name)