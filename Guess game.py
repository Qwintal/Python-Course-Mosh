#  Make a guess game, give 3 chances and then print msg.

secret_number = 1
number_of_guess = 0
maximum_number_of_guess = 3

while number_of_guess < maximum_number_of_guess:
    guess = int(input("Guess: "))
    number_of_guess += 1
    if guess == secret_number:
        print("Congratulation you guess right!")
        break

else:
    print("Sorry you guessed all wrong =(")


# Important things to focus on:
# Learn to give variable.
# Try to write code like a story.
# Give proper variable naming to increase productivity and that everything is clear.
