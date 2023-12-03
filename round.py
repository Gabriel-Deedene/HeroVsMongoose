# Basic libraries.
import random

# Local libraries.
from entity import Entity
    
class Round:
    """
    This class represents a round of the fight between Peter and the mongooses.

    Attributes:
    - player (Entity): Class.
    - enemy (Entity): Class.
    - winner (String): name of fight winner.
    """

    def __init__(self, player: Entity, enemy: Entity):
        """
        Initialize a round instance.

        Parameters:
        - player (Entity): Class.
        - enemy (Entity): Class.
        - winner (String): name of fight winner.

        Returns:
        None
        """

        self.player = player
        self.enemy = enemy
        self.winner = ""
        self.compteurCapacitySnakeEyes = 0
        self.lastRecoursCapacityUsed = False
    
    

    ########## Player Control ##########

    def fightPlayer(self):
        """
        attaque basique, randint qui désigne une valeur de damange entre le min et le max. 
        Puis l'inflige à l'entité en question.
        
        Parameters:
        - self

        Returns:
        damage
        """

        damage=random.randint(self.player.minDamage, self.player.maxDamage)
        newHp=self.enemy.hp-damage
        self.enemy.hp=newHp
        return (damage)
        

    def basicAttackPlayer(self):
        """
        Def qui regroupe l'attaque du joueur plus l'affichage dans le terminal.
        
        Parameters:
        - self

        Returns:
        None
        """

        damage = self.fightPlayer()
        print("")
        print(f"{self.player.name} commence avec {self.player.minDamage} a {self.player.maxDamage} degats.\nUn jet aléatoire nous donne {damage}\n\n{self.enemy.name} n'a pas d'armure.\n{self.enemy.name} perd {damage} points de vie. Le total de points de vie après l'attaque est {self.enemy.hp}.")


    def defenseCapacity(self):
        """
        capacité de se protéger. 
        x2 au niveau bouclier.
        Et si hp pair, alors attaque basique en plus.
        Avec un affichage dans le terminal.
        
        Parameters:
        - self

        Returns:
        None
        """

        self.player.armor = self.player.armor*2
        if (self.player.hp % 2) == 0:
            self.basicAttackPlayer()
        print(f"La capacité de defense est activée, l'armure de {self.player.name} est multiplié par 2 soit : {self.player.armor}")


    def snakeEyesCapacity(self,round: int):
        """
        Permet de se régénerer selon certaines règles :
        pas plus de deux "1" du nombre binaire des pv de l'enemie.
        Le skill met 2 rounds pour se recharger
        
        Parameters:
        - self
        - round (int):  nombre de rounds dans le combat, pour voir s'il est possible d'utiliser la capacité

        Returns:
        None
        """

        if (round - self.compteurCapacitySnakeEyes > 2 ):

            self.compteurCapacitySnakeEyes = round

            #regarde le nombre de 1 dans le nombre binaire des hp de l'ennemie
            binHpEnemy = str(bin(self.enemy.hp))
            count_of_1 = 0
            for number in binHpEnemy:
                if number == "1":
                    count_of_1 += 1

            if (count_of_1<=2):
                #Attaque basique
                damage = self.fightPlayer()
                print(f"{self.player.name} commence avec {self.player.minDamage} a {self.player.maxDamage} degats.\nUn jet aléatoire nous donne {damage}\n\n{self.enemy.name} n'a pas d'armure.\n{self.enemy.name} perd {damage} points de vie. Le total de points de vie après l'attaque est {self.enemy.hp}.")

                #système de régéneration
                self.player.hp += damage
                if (self.player.hp > self.player.hpMax):
                    self.player.hp = self.player.hpMax

        else :
            print("La capacité Snake Eyes doit se recharger pendant 2 rounds, à la place, une attaque basique est lancée !")
            self.basicAttackPlayer()


    def lastRecoursCapacity(self):
        """
        Fait les dégâts maximum possible, multipliés par 3, mais rate parfois sa cible.
        La chance de toucher est proportionnelle au pourcentage de points de vie perdus.
        Peut être utilisé qu'une seule fois.
        
        Parameters:
        - self

        Returns:
        None
        """

        #check si déjà utilisé
        if (self.lastRecoursCapacityUsed == False):
            self.lastRecoursCapacityUsed = True

            #aléatoire pour savoir si l'attaque va toucher
            tryToAttack = random.randint(1,self.player.hpMax)

            #si l'attaque à la chance de toucher
            if (tryToAttack > self.player.hp):
                damage = self.player.maxDamage * 3
                newHp=self.enemy.hp-damage
                self.enemy.hp=newHp
                print(f"{self.player.name} touche son attaque de dernier recours ! {self.enemy.name} n'a pas d'armure.\n{self.enemy.name} perd {damage} points de vie. Le total de points de vie après l'attaque est {self.enemy.hp}.")
            #sinon, c'est loupé, déso
            else:
                print("L'attaque de dernier recours à loupée sa cible.")

        #si l'attaque a déjà été utilisé pendant le combat, alors cela lance une attaque basique
        else : 
            print("La capacité dernier recours ne peut être utilisée qu'une seule fois par combat, à la place, une attaque basique est lancée !")
            self.basicAttackPlayer()



    ########## Enemy Control ##########

    def fightEnemy(self):
        """
        Attaque basique de l'enemie, randint qui désigne une valeur de damange entre le min et le max. 
        Puis l'inflige à l'entité en question.
        
        Parameters:
        - self

        Returns:
        None
        """

        damage=random.randint(self.enemy.minDamage, self.enemy.maxDamage)
        newHp=self.player.hp-(damage-self.player.armor)
        self.player.hp=newHp
        return (damage)

    def basicAttackEnemy(self):
        """
        Def qui regroupe l'attaque de l'enemie plus l'affichage dans le terminal.
        
        Parameters:
        - self

        Returns:
        None
        """

        damage = self.fightEnemy()
        if (damage < 0):
            damage = 0
        print("")
        print(f"{self.enemy.name} commence avec {self.enemy.minDamage} a {self.enemy.maxDamage} degats.\nUn jet aléatoire nous donne {damage}\n\n{self.player.name} a une valeure d'armure de {self.player.armor}.\n{self.player.name} perd {(damage-self.player.armor)} points de vie. Le total de points de vie après l'attaque est {self.player.hp}.")
        self.testWin()
        if self.winner != "":
            runBattle = False



    ########## Over Control ##########

    def testWin(self):
        """
        Test s'il y a un gagnant en vérifiant les hp de chacun.
        Retourne le nom du gagnant
        
        Parameters:
        - self

        Returns:
        self.winner
        """

        if self.enemy.hp <= 0:
            self.winner = self.player.name
            print (f"{self.player.name} est le gagnant !")
            print (self.winner)
            return (self.winner)
        elif self.player.hp <= 0:
            self.winner = self.enemy.name
            print (f"{self.enemy.name} est le gagnant !")
            return (self.winner)

