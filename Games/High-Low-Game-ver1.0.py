import random


class HighLow:
    """ROCK IT!!!"""

    def __init__(self):
        """Init Test"""
        self.secretNumber = 0
        self.tries = 5
        self.guessed = False

    def PlayGame(self):
        """Begins the game of High Low"""
        self.secretNumber = random.randint(1, 10)

        print("Welcome to HIGH/LOW game!")
        print("You have 5 tries to guess the number!!.")
        print("\n")

        while not self.guessed and self.tries > 0:

            guess = int(input("What is your guess? "))
            self.tries -= 1

            if guess < self.secretNumber:
                print("Too low!")
            elif guess > self.secretNumber:
                print("Too high!")
            else:
                print("Correct!")
                self.guessed = True

        if not self.guessed:
            print("Game over!")
        else:
            print("Congrats!")


if __name__ == '__main__':
    newGame = HighLow()
    newGame.PlayGame()