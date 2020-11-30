# Example 1
i = 1

while i <= 5:
    print('*' * i)
    i = i + 1

# Example 2

secret_num = 9
num_guess = 1
guess_limit = 3
while num_guess <= guess_limit:
    input_num = int(input("guess the secret number: "))
    if input_num == secret_num:
        print("Bam! You guessed right")
        break
    else:
        if num_guess == guess_limit:
            print("Number of guesses over, you LOSE!")
    num_guess = num_guess + 1
else :
    print('\n')
    print('Try again!')


print("\nGAME OVER")

# Test Exercise 01


while True:
    user_command = input("> ").lower()
    if user_command == 'help':
        print(''' start --> start the car
 stop --> stop the car
 quit --> exit the game
        ''')
    elif user_command == 'start':
        print("Car started, vooooo")
    elif user_command == 'stop':
        print("Car is stopping")
    elif user_command == 'quit':
        print("Exiting the game")
        break
    else:
        print("I don't understand this command")
