# Basic libraries.
import datetime

# Local libraries.
from battle import Battle
from round import Round
from entity import Entity

########## Variables ##########
gameOn = True
score = 0
player=Entity("Peter",20,3,6,1,1,True)
enemy=Entity("Mongoose",10,1,2)


def main(player,enemy,score):                
    
    roundBattle=Round(player,enemy)
    fight=Battle(roundBattle)
    
    winner=fight.run()

    if (winner != player.name):
        print("Vous avez perdu...")

    else :
        score += 1
        print("")
        chooseContinue = input("Voulez-vous continuer l'aventure -> 'o' ou arréter et retourner en ville -> 'n'\nIndiquez votre choix : ")
        print("")

        match chooseContinue:
            case "o":

                if (score != 0):
                    enemy.hpMax += 3
                    enemy.hp = enemy.hpMax

                    if (score % 2) != 0:
                        enemy.maxDamage += 3
                        enemy.minDamage += 3

                print("")
                print(f"Voici les statistiques de {player.name}:\nDégats entre {player.minDamage} et {player.maxDamage}, il a {player.hp}/{player.hpMax} hp et {player.armor} d'armure.")
                print("")
                chooseAfterFight = input(f"{player.name} à le temps de faire une manipulation avant son prochain combat :\nAugmenter les dégâts max -> 'a' ou min -> 'i', augmenter son armure -> 's' ou regagner des pv -> 'h'\nQue faites-vous : ")
                print("")

                match chooseAfterFight:
                    case "a":
                        player.maxDamage += 2
                        print(f"Vous augmentez vos dégâts max grâce à l'un des crocs de l'enemie : {player.maxDamage}")
                    case "i":
                        player.minDamage += 3
                        if (player.minDamage > player.maxDamage):
                            player.minDamage = player.maxDamage
                        print(f"Vous augmentez vos dégâts min grâce à l'une des griffes de l'enemie : {player.minDamage}")
                    case "s":
                        player.armorMax += 1
                        player.armor = player.armorMax
                        print(f"Vous augmentez votre armure de 1 grâce au cuir de l'enemie : {player.armor}")
                    case "h":
                        if (player.snack):
                            player.snack = False
                            player.hp += 10
                            if (player.hp > player.hpMax):
                                player.hp = player.hpMax
                            print(f"{player.name} se soigne de 10, il possède maitenant : {player.hp}/{player.hpMax} hp")
                        else :
                            player.snack = True
                            print("Il n'y avait plus de gouter, vous avez récupéré la viande de l'enemie et l'avait fait cuire ! Il faudra attendre un autre tour pour la manger")

                main(player,enemy,score)

            case "n":
                print(f"Le score de votre partie est de {score} ! Félicitations")

                print("ajout du score pas encore possible, ça arrive soon !")
                # filenameScore = "scores.txt"
                # f = open(filenameScore, "r+")

                # compteurLigne = 0
                # for line in f.readlines():
                #     if (score > int(line[0])):
                #        namePlayer = input("Veuillez entrer votre nom")
                #        f.write(f"{score} - by {namePlayer} - {datetime.date()}")
                #     compteurLigne += 1

                # f.close



while gameOn:
    chooseMenu = input("Que souhaitez-vous faire ?\nNew Game -> 'n' | Best scores -> 's' | Credits -> 'c' | Quit -> 'q'\nQuelle est votre choix : ")
    print("")

    match chooseMenu:
        case "n":
            main(player,enemy,score)
        case "s":
            filenameScore = "scores.txt"
            f = open(filenameScore, "r+")
            for line in f.readlines():
                print (line)
            print("")
            f.close
        case "c":
            print("\nGame create by Gabriel Deedene, the lord of yogurt.\n\n")
        case "q":
            gameOn = False
            print("Bye bye")