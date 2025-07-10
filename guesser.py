import random

play_again = "play"

while play_again == "play":
    secret_number = random.randint(1, 10)
    number = int(input("Guess a number from 1 to 10: "))
    accuracy = 100
    attempt = 0

    while number != secret_number:
        print("Wrong! Please Retry.")
        number = int(input("Enter a new value > "))
        attempt += 10
        if number <= 10 :
         break 
        print("invalid number")

    print(f"Congratulations! You guessed it right. The number was: {secret_number}.")
    print(f"Your accuracy is: {accuracy - attempt}%")

    play_again = input("Wanna play again? Enter 'play' to continue, or anything else to quit: ")

print("End Of The Game.")

