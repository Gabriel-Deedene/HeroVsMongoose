class Capacity:
    """
    This class represents all capacitys of the hero.

    Attributes:
    - name (String): name of the capacity.
    - multiplicatorDamage (Int): multiplicator of damages.
    - multiplicatorArmor (Int): multiplicator of the armor.
    """

    def __init__(self, name, multiplicatorDamage):
        """
        Initialize a capacity instance.

        Parameters:
        - name (String): name of the capacity.
        - multiplicatorDamage (Int): multiplicator of damages.
        - multiplicatorArmor (Int): multiplicator of the armor.

        Returns:
        None
        """
        self.name = name
        self.multiplicatorDamage = 3
        self.multiplicatorArmor = 2
        
    

    def useCapacity (self):
        print("test")
        #trouver dans la doc python le moyen de choisir selon le nom de la capacité envoyé (au lieu d'utiliser des "if")


    def Defence(self):
        print("Defence")
        #definition defence à trouver

    #faire 3 instances qui sont constantes