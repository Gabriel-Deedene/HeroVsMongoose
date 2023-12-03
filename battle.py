# Local libraries.
from round import Round

    
class Battle:
    """
    This class represents an entire fight between Peter and a mongoose.

    Attributes:
    - round (Round): Class.
    - nbRounds (Int): The number of rounds.
    """

    def __init__(self, round: Round):
        """
        Initialize a battle instance.

        Parameters:
        - round (Round): Class.
        - nbRounds (Int): The number of rounds.

        Returns:
        None
        """
        self.round = round
        self.nbRounds = 0
    
    
    def run(self):
        """
        Permet de faire un combat complet en bouclant la classe round.

        Parameters:
        - /

        Returns:
        self.round.winner
        """
        
        #booleen pour savoir quand il faut s'arréter de boucler le combat (utilisé juste en dessous)
        runBattle = True

        while runBattle:
            #affichage du nombre de tour
            print(f"Nouveau tour : {self.nbRounds}\n\n")

            #si capacité defense utilisé, alors dans nouveau round, élimination du boost de défence
            if (self.round.player.armor>self.round.player.armorMax):
                self.round.player.armor = self.round.player.armorMax
                print(f"Debut du nouveau tour, {self.round.player.name} perd son bonus d'armure qui se réduit de moitié : soit {self.round.player.armor}\n")

            #Choisir la capacité à utliser sur le round
            print("")
            chooseAttack = input(f"C'est au tour de {self.round.player.name} de jouer, que voulez-vous faire ?\nAttaque basique = 'a', Defense = 'z', Snake eyes = 'e', Dernier recours = 'r'\nQuelle compétence vous souhaitez utiliser : ")
            print("")

            match chooseAttack:
                #toujours le même fonctionnement, selon la valeur de l'input, il appelle une fonction présente dans la classe Round
                case "a":
                    self.round.basicAttackPlayer()
                case "z":
                    self.round.defenseCapacity()
                case "e":
                    self.round.snakeEyesCapacity(self.nbRounds)
                case "r":
                    self.round.lastRecoursCapacity()

            #test si le joueur ou son enemie à gagné
            self.round.testWin()
            if self.round.winner != "":
                runBattle = False

            #Winner detection for player -> break pour éviter de faire jouer l'enemie alors qu'il est déjà mort
            if self.round.winner == self.round.player.name:
                break
            
            #attaque basique de l'enemie
            self.round.basicAttackEnemy()

            #Winner detection for enemy
            if self.round.winner == self.round.player.name:
                print ("ERROR - DETECTION WIN BROKEN") #because in this case, it is the enemy who wins

            self.nbRounds += 1
        

        return self.round.winner
    