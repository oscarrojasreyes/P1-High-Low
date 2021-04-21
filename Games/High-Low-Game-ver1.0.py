import random


class HighLow:
    """ROCK IT!!!"""
    def __init__(self):
        """Init Test"""
        self.secretNumber = 0
        self.tries = 5
        self.difficulty = 0
        self.guessed = False

    def setdifficulty(self):
        _a = [8, 5, 3, 1]
        print("What difficulty would you like to play with?\n"
              "[1] Easy - 8 guesses\n"
              "[2] Medium - 5 guesses\n"
              "[3] Hard - 3 guesses\n"
              "[4] Insane - 1 guess")
        while self.difficulty not in [1, 2, 3, 4]:
            self.difficulty = int(input("Choice: "))
        self.tries = _a[self.difficulty-1]

    def playgame(self):
        """Begins the game of High Low"""
        self.secretNumber = random.randint(1,10)

        print("Welcome to Higher / Lower game!")

        self.setdifficulty()
        
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
