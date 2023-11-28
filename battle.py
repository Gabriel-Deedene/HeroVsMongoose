# Local libraries.
from round import Round
from entity import Entity
    
class Battle:
    """
    This class represents an entire fight between Peter and a mongoose.

    Attributes:
    - round (Round): Class.
    - score (Int): The number of victories.
    """

    def __init__(self, round: Round):
        """
        Initialize a battle instance.

        Parameters:
        - round (Round): Class.
        - score (Int): The number of victories.

        Returns:
        None
        """
        self.round = round
        self.score = 0
    
    
    def run(self):
        """
        boucle (à revoir)

        Parameters:
        - /

        Returns:
        self.round.winner
        """
        
        runBattle = True

        while runBattle:
            
            if (self.round.player.armor>self.round.player.armorMax):
                self.round.player.armor = self.round.player.armorMax
                print(f"Debut du nouveau tour, {self.round.player.name} perd son bonus d'armure qui se réduit de moitié : soit {self.round.player.armor}")


            print(self.round.basicAttackPlayer())

            #Winner detection for player
            if self.round.winner == f"{self.round.player.name} est le gagnant !":
                self.score = self.score + 1
                break


            print(self.round.basicAttackEnemy())

            #Winner detection for enemy
            if self.round.winner == f"{self.round.player.name} est le gagnant !":
                print ("ERROR - DETECTION WIN BROKEN") #because in this case, it is the enemy who wins
        

        return self.round.winner, self.score
    

hero=Entity("Galdric",20,3,6,1,1,True)
ratus=Entity("ratus",10,1,2)
first=Round(hero,ratus)
firstbattle=Battle(first)

print (firstbattle.run())
