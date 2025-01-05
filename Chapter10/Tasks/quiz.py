file_name = 'users_quiz.txt'

print("Why do you like coding?\n" + "Press 'Enter' for quit.")

while True:
    with open(file_name, 'a') as file_object:
        answer = input("Your answer: ")
        if answer != '':
            file_object.write(answer + '\n')
        else: break