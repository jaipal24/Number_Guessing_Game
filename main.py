import math
import random
if __name__ == '__main__':
    # Reading the range
    name = input("Please enter the player name:")
    start, end = map(int, input("Please enter the range(Example: 1 20) {0}:".format(name)).split(" "))
    min_guess = math.log(end-start+1, 2)
    print("\n\tYou've only ", round(math.log(end - start + 1, 2)), " chances to guess the integer!\n")
    res = random.randint(start, end)
    count = 0
    while count < min_guess:
        guess = int(input("{0} please make your guess:".format(name)))
        if guess > res:
            print("Try Again! You guessed too high")
            count += 1
        elif guess < res:
            print("Try Again! You guessed too small")
            count += 1
        else:
            count += 1
            if count <= min_guess:
                print("Congratulations! {0}".format(name))
                break
    if count > min_guess:
        print("Sorry {0} you have crossed min guesses.Better Luck Next Time!".format(name))
