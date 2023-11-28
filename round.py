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
    
    
    def fightPlayer(self):
        damage=random.randint(self.player.minDamage, self.player.maxDamage)
        newHp=self.enemy.hp-damage
        self.enemy.hp=newHp
        result=f"{self.player.name} commence avec {self.player.minDamage} a {self.player.maxDamage} degats.\nUn jet aléatoire nous donne {damage}\n\n{self.enemy.name} n'a pas d'armure.\n{self.enemy.name} perd {damage} points de vie. Le total de points de vie après l'attaque est {self.enemy.hp}."
        return (result)
        
    def testWinPlayer(self):
        if self.enemy.hp <= 0:
            self.winner = f"{self.player.name} est le gagnant !"
            return (self.winner)

    def fightEnemy(self):
        damage=random.randint(self.enemy.minDamage, self.enemy.maxDamage)
        newHp=self.player.hp-(damage-self.player.armor)
        self.player.hp=newHp
        result=f"{self.enemy.name} commence avec {self.enemy.minDamage} a {self.enemy.maxDamage} degats.\nUn jet aléatoire nous donne {damage}\n\n{self.player.name} a une valeure d'armure de {self.player.armor}.\n{self.player.name} perd {(damage-self.player.armor)} points de vie. Le total de points de vie après l'attaque est {self.player.hp}."
        return (result)
        
    def testWinEnemy(self):
        if self.player.hp <= 0:
            self.winner = f"{self.enemy.name} est le gagnant !"
            return (self.winner)



# hero=Entity("hero",20,3,6,1,True)
# ratus=Entity("ratus",10,1,2,0,False)

# print (first.fightPlayer())
