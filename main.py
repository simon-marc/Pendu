import  pygame, sys , Hangman
hm = Hangman.Hangman()
print(hm.wordList, hm.guessList)
from pygame.locals import QUIT

pygame.init()

#Définition de la fenêtre de jeu
HANGMANWINDOW = pygame.display.set_mode((500, 300))
pygame.display.set_caption('Python Game')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Times',22, False, False)


#Fonction concernant l'avancement des stages en focntions des erreurs de l'utilisateur
def drawHangman(stage):
    if stage > 6:
        stage = 6
    img = pygame.image.load(str(stage)+".png")
    img = pygame.transform.scale(img, (150,200))
    HANGMANWINDOW.blit(img, (0,0))
    
#Fonction pour afficher un message dans les deux cas de figure : Win or Lose, ainsi que les pointillets pour insérer les lettres désirées.
def drawWord():
    status = hm.gameStatus()
    if status == 0:
        textSurface = font.render("Type your Guess in Lowercase",False, 'black')
    elif status == 1:
        textSurface = font.render("You won ! Press ESC for restarting",False, 'black')
    else:
        textSurface = font.render("You lost ! Press ESC for restarting",False, 'black')

    HANGMANWINDOW.blit(textSurface,(180,50))
    word = ""
    for g in hm.guessList:
        word = word + g + "  "
    textSurface = font.render(word,False, 'black')
    HANGMANWINDOW.blit(textSurface,(220,100))

    textSurface = font.render('Words already used',False, 'black')
    HANGMANWINDOW.blit(textSurface,(180,150))

    word = ""
    for g in hm.pastGuess:
        word = word + g + "  "
    textSurface = font.render(word,False, 'black')
    HANGMANWINDOW.blit(textSurface,(200,200))

    


while True:
    HANGMANWINDOW.fill('lightgrey')
    drawHangman(hm.guessCount)
    drawWord()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if str(event.unicode).isalpha() :
                hm.checkWord(str(event.unicode))
            elif event.key == pygame.K_ESCAPE:
                hm.restartGame()
    pygame.display.update()
    clock.tick(60)

