import random


class HighLow:
    """ROCK IT!!!"""

    def __init__(self):
        """Init Test"""
        self.secretNumber = 0
        self.tries = 5
        self.difficulty = 0
        self.range = 0
        self.guessed = False

    def setdifficulty(self):
        _a = [8, 5, 3, 1]
        print("What difficulty would you like to play with?\n"
              "[1] Easy - 8 guesses\n"
              "[2] Medium - 5 guesses\n"
              "[3] Hard - 3 guesses\n"
              "[4] Insane - 1 guess")
        while self.difficulty not in [1, 2, 3, 4]:
            try:
                self.difficulty = int(input("Choice: "))
            except ValueError:
                print("that's not a number, silly")
        self.tries = _a[self.difficulty - 1]

    def setrange(self):
        while self.range == 0:
            range = input("How many numbers do you want to guess from? ")
            if range:
                try:
                    self.range = int(range)
                except ValueError:
                    print("that's not a number, silly")
            else:
                self.range = 10

    def playgame(self):
        """Begins the game of High Low"""

        print("Welcome to Higher / Lower game!")

        self.setdifficulty()

        self.setrange()

        self.secretNumber = random.randint(1, self.range)

        while not self.guessed and self.tries > 0:
            print("Try to guess the secret number...")
            guess = int(input(f"You have {self.tries} more tries. What is your guess? "))
            self.tries -= 1

            if guess < self.secretNumber and self.tries > 0:
                print("Too low!")
            elif guess > self.secretNumber and self.tries > 0:
                print("Too high!")
            else:
                print("Correct!")
                self.guessed = True

        if not self.guessed:
            print(f"Game over! The secret number was {self.secretNumber}")
        else:
            print("Congrats!")


if __name__ == '__main__':
    newGame = HighLow()
    newGame.playgame()
