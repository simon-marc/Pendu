import random
#Definition de la classe
class Hangman:
    def __init__(self, word=""):
        self.word = word
        if len(word)<=3:
            self.word = self.pickAword()
        self.wordList = [self.word[i] for i in range(len(self.word))]
        self.guessList = ['-' for _ in range(len(self.word))]
        self.pastGuess = []
        self.guessCount = 0

#Fonction pour reboot le jeu une fois que l'on a gagné ou perdu
    def restartGame(self):
        self.word = self.pickAword()
        self.wordList = [self.word[i] for i in range(len(self.word))]
        self.guessList = ['-' for _ in range(len(self.word))]
        self.pastGuess = []
        self.guessCount = 0
        
#Fonction qui permet de definir la limite d'essai en fonction des stages affichés à l'écran
    def gameStatus(self):
        if self.guessList.count('-') == 0:
            return 1
        elif self.guessCount == 6:
            return 2
        else:
            return 0

#Fonction pour choisir un mot au hasard dans le fichier .txt
    def pickAword(self):
        f = open("words.txt")
        for line in f :
            words = line.split(",")
        wordCollection = []
        for word in words:
            word = word.strip()
            word = word[1: -1]
            wordCollection.append(word)
        print(wordCollection)
        return random.choice(wordCollection)
    def checkWord(self,guess):
        if self.gameStatus()!=0:
            return False
        result = False
        if guess not in self.pastGuess:
            self.pastGuess.append(guess)
        else:
            return

        for i,ch in enumerate(self.wordList):
            if guess == ch:
                self.guessList[i] = ch
                result = True
        if result == False:
            self.guessCount +=1

        return result