#importation random pr tirage au sort et time pr minuter la réponse
import random
import time

#déclaration des valeurs
rock = 1
paper = 2
scissors = 3

names = {rock: "Caillou", paper: "Papier", scissors: "Ciseaux"}
rules = {rock: scissors, paper: rock, scissors: paper}

#compte score
player_score = 0
computer_score = 0

#définition de la fonction start
def start():
    print("On va jouer a chifoumi")
    while game():
        pass
    scores()

# définition du move où on choisit son coup
def move():
    while True:
        print
        player = input("Caillou = 1\nPapier = 2\nCiseaux = 3\n Make a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print(" O_o on a dit un 1 2 ou 3!")

# définition du temps de résultat et du suspens
def result(player, computer):
    print ("chi...")
    time.sleep(1)
    print ("fou...")
    time.sleep(1)
    print ("MI!")
    time.sleep(0.5)
    print ("computer threw {0} !".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print ("Tie Game")
    else:
        if rules[player] == computer:
            print ("Tu as gagné")
            player_score += 1
        else:
            print ("La Machine gagne toujours!!!")
            computer_score += 1

# définition de rejouer
def play_again():
    answer= input("Une autre partie? y/n: ")
    if answer in ("y", "Y", "yes", "oui", "OH OUI!") :
        return answer
    else:
        print ("Bon ben tant pis bisous!")

# définition du calcul des scores
def scores():
    global player_score, computer_score
    print ("High Scores")
    print ("Player", player_score)
    print ("Computer", computer_score)

# Architecture globale du jeu
def game():
    player=move()
    computer=random.randint(1,3)
    result(player,computer)
    return play_again()


if __name__ == '__main__':
    start()

