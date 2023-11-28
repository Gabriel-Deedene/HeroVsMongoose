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


    def __str__(self) -> str:
        return f"stop"
    
    
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

            print(self.round.fightPlayer())
            self.round.testWinPlayer()

            if self.round.winner != "":
                runBattle = False
                if self.round.winner == f"{self.round.player.name} est le gagnant !":
                    self.score = self.score + 1
                break

            print(self.round.fightEnemy())
            self.round.testWinEnemy()

            if self.round.winner != "":
                runBattle = False
                if self.round.winner == f"{self.round.player.name} est le gagnant !":
                    print ("ERROR - DETECTION WIN BROKEN")
        
        return self.round.winner, self.score
    

hero=Entity("Galdric",20,3,6,1,True)
ratus=Entity("ratus",10,1,2,0,False)
first=Round(hero,ratus)
firstbattle=Battle(first)

print (firstbattle.run())
