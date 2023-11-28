from entity import Entity

class Capacity:
    """
    This class represents all capacitys of the hero.

    Attributes:
    - name (String): name of the capacity.
    - multiplicatorDamage (Int): multiplicator of damages.
    - multiplicatorArmor (Int): multiplicator of the armor.
    """

    def __init__(self, name, multiplicatorDamage, multiplicatorArmor):
        """
        Initialize a capacity instance.

        Parameters:
        - name (String): name of the capacity.
        - multiplicatorDamage (Int): multiplicator of damages.
        - multiplicatorArmor (Int): multiplicator of the armor.

        Returns:
        None
        """
        self.name = ""
        self.multiplicatorDamage = multiplicatorDamage
        self.multiplicatorArmor = multiplicatorArmor
        

    def __str__(self) -> str:
        return f"stop"
    

    def useCapacity (self):
        print("test")
        #trouver dans la doc python le moyen de choisir selon le nom de la capacité envoyé (au lieu d'utiliser des "if")