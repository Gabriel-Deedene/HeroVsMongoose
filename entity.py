class Entity:
    """
    This class represents an entity, the hero and/or the enemy.

    Attributes:
    - name (String): name of the capacity.
    - multiplicatorDamage (Int): multiplicator of damages.
    - multiplicatorArmor (Int): multiplicator of the armor.
    """
        
    def __init__(self, name, hpMax, minDamage, maxDamage, armorMax = 0, armor = 0, snack = False):
        """
        Initialize a entity instance.

        Parameters:
        - name (String): The name of the entity.
        - hpMax (Int): The maximal Health Point of the entity.
        - hp (Int): The curent Health Point of the entity.
        - minDamage (Int): Class.
        - maxDamage (Int): Class.
        - armorMax (int): The maximum of armor.
        - armor (Int): The curent armor.
        - snack (Booleen): To know if Peter have a snack or not.

        Returns:
        None
        """
        
        self.name = name
        self.hpMax = hpMax
        self.hp = hpMax
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.armorMax = armorMax
        self.armor = armor
        self.snack = snack

    def __str__(self) -> str:
        return f"{self.name} a {self.hp} HP, il fait entre {self.minDamage} et {self.maxDamage} de dégâts par coup d'épée. Son armure le protège de {self.armor} et son goûter est {self.snack}"