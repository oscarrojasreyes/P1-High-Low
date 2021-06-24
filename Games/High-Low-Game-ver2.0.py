import random

from Module.breezypythongui import EasyFrame, EasyDialog


class HighLow(EasyFrame):
    """A game of High/Low"""
    def __init__(self):
        self.difficulty = 0
        EasyFrame.__init__(self, "Title")
        self.outputArea = self.addCanvas(width=300,height=200)

        self.WelcomeText = self.outputArea.drawText("Welcome to High / Low!", x=150, y=195, font=('Arial',8))
        self.outputArea.drawRectangle(5, 5, 125, 175)
        self.outputArea.drawRectangle(295, 5, 295-120, 175)
        self.xText = self.outputArea.drawText("?", 65, 95, font=('Arial',80))
        self.yText = self.outputArea.drawText("?", 235, 95, font=('Arial',80))

        self.playButton = self.addButton(text="Play Game", row=1, column=0, state="disabled",
                                         command=self.playGame)
        self.diffButton = self.addButton(text="Set Difficulty", row=2, column=0,
                       command=self.setDifficulty)

    def setDifficulty(self):
        difficultyDialog = DifficultyDialog(self, self.difficulty)
        if difficultyDialog.modified():
            self.difficulty = difficultyDialog.difficulty
            self.playButton.__setitem__("state", "active")
            print(self.difficulty)

    def playGame(self):
        gameWindow = MainGameWindow(self.difficulty)
        EasyFrame.destroy(self)


class MainGameWindow(EasyFrame):
    def __init__(self, diff):
        self.lives = diff
        self.cardDisplay = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.x = random.randint(1,14)
        self.y = random.randint(1,14)
        while self.y == self.x:
            self.y = random.randint(1,14)

        EasyFrame.__init__(self, f"High/Low - Lives: {self.lives}")
        self.outputArea = self.addCanvas(width=300, height=200)
        self.outputArea.drawRectangle(5, 5, 125, 175)
        self.outputArea.drawRectangle(295, 5, 295-120, 175)
        self.GuessText = self.outputArea.drawText("Is the hidden card higher or lower?", x=150, y=195, font=('Arial', 8))
        self.xText = self.outputArea.drawText(self.cardDisplay[self.x-1], 65, 95, font=('Arial', 80))
        self.yText = self.outputArea.drawText("?", 235, 95, font=('Arial',80))
        self.higherButton = self.addButton(text="Higher", row=1, column=0,
                                         command=self.guessHigh)
        self.lowerButton = self.addButton(text="Lower", row=2, column=0,
                       command=self.guessLow)

    def guessHigh(self):
        guessDialog = GuessDialog(self, self.x, self.y, self.lives, True)
        if guessDialog.modified():
            self.lives = self.lives - 1

        if self.lives > -1:
            gameWindow = MainGameWindow(self.lives)
        else:
            exit()
        EasyFrame.destroy(self)

    def guessLow(self):
        guessDialog = GuessDialog(self, self.x, self.y, self.lives, False)
        if guessDialog.modified():
            self.lives = self.lives - 1

        if self.lives > -1:
            gameWindow = MainGameWindow(self.lives)
        else:
            exit()
        EasyFrame.destroy(self)

    def ShitYourself(self):
        exit()

class DifficultyDialog(EasyDialog):
    def __init__(self, parent, difficulty):
        self.parent = parent
        self.difficulty = difficulty
        self._ = None
        EasyDialog.__init__(self, parent, "Set Difficulty")

    def body(self, master):
        self._ = self.addRadiobuttonGroup(master, row=0, column=0)
        self._.addRadiobutton(text="Easy")
        default = self._.addRadiobutton(text="Medium")
        self._.addRadiobutton(text="Hard")
        self._.setSelectedButton(default)

    def apply(self):
        x = self._.getSelectedButton()["text"]
        if x == "Easy":
            self.difficulty = 10
        elif x == "Medium":
            self.difficulty = 5
        elif x == "Hard":
            self.difficulty = 3
        self.setModified()


class GuessDialog(EasyDialog):
    def __init__(self, parent, x, y, lives, guessedHigherBool):
        self.parent = parent
        self.x = x
        self.y = y
        self.cardDisplay = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self._ = None
        self.guessedHigh = guessedHigherBool
        self.correct = None

        EasyDialog.__init__(self, parent, "You've guessed...")

    def body(self, master):
        if (self.guessedHigh and self.x < self.y) or (not self.guessedHigh and self.y < self.x):
            self.addLabel(master, f"Your Card: {self.cardDisplay[self.x-1]}\nHidden Card: {self.cardDisplay[self.y-1]}\nYou guessed correctly!",row=0, column=0)
            self.correct = True
        else:
            self.addLabel(master, f"Your Card: {self.cardDisplay[self.x-1]}\nHidden Card: {self.cardDisplay[self.y-1]}\nMaybe next time!",row=0, column=0)
            self.correct = False

    def apply(self):
        if not self.correct:
            self.setModified()


if __name__ == "__main__":
    HighLow().mainloop()