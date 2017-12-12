from random import randint

from observer.observer import Observer
from observable.observable import Observable

class Monster(Observable):
    """
    Class that creates a monster object.
    
    A monster is an observable, and has a name, health, and attack damage
    attributes. This is a parent class that is intended to be
    instantiated through one of its child classes (Person, Zombie,
    Vampire, Ghoul, or Werewolve).
    """

    _monster_count = 0

    def __init__(self, name, health, attack_dmg):
        """
        Class that creates a monster object.
    
        Args:
            name: Name of the type of monster.
            health: Monsters health.
            attack_dmg: The amount of damage the monster attacks with.
        """
        super().__init__()
        self._name = name
        self._health = health	
        self._attack_dmg = attack_dmg

    @property
    def name(self):
        """
        Getter method for the name instance attribute.
    
        Returns:
            The name of the monster.
        """
        return self._name

    #Could not decorate this as a property because the setter
    #requires you to replace the value and I wanted it to update
    #the existing value.	
    def get_health(self):
        """
        Getter method for the health instance attribute.
    
        Returns:
            The health of the monster.
        """
        return self._health

    def set_health(self, damage):
        """
        Setter method for the health instance attribute.
        
        Args:
            damage: The amount of damage taken when attacked.
        """
        self._health += damage

    @property
    def attack_dmg(self):
        """
        Getter method for the attack damage instance attribute.
    
        Returns:
            Returns the attack damage of the monster.
        """
        return self._attack_dmg

    def add_monster(self):
        """
        Method that adds one to the total count of monsters instantiated.
    
        """
        Monster._monster_count += 1

    def remove_monster(self):
        """
        Method that removes one from the total count of monsters instantiated.
    
        """
        Monster._monster_count -= 1

    def monsters_remaining(self):
        """
        Method that returns the total number of monsters that are still alive.
    
        Returns:
            Returns the total number of monsters.
        """
        return Monster._monster_count

    def is_alive(self):
        """
        Method that checks to see if a monsters health is greater than 0.

        Returns:
            Returns True if the monster is still alive else returns False.
        """
        return self._health > 0
        
class Person(Monster):
    """
    Class that creates a Person monster.
    """

    def __init__(self, name="Person", health=100, attack_dmg=2):
        """
        Constructor that calls the parent constructor and 
        initializes a Person object.

        Args:
            name: Name of the type of monster.
            health: Monsters health.
            attack_dmg: The amount of damage the monster attacks with.
        """
        super().__init__(name, health, attack_dmg):


class Zombie(Monster):
    """
    Class that creates a Zombie monster.
    """

    def __init__(self, name="Zombie", health=100, attack_dmg=-1):
        """
        Constructor that calls the parent constructor and 
        initializes a Zombie object.

        Args:
            name: Name of the type of monster.
            health: Monsters health.
            attack_dmg: The amount of damage the monster attacks with.
        """
        super().__init__(name, health, attack_dmg)
        self.add_monster()

    #TODO: A lot of repetitive code, could possibly move this method in 
    #the parent class in the future.
    def take_damage(self, attack_dmg, weapon):
        """
        Method that is responsible for updating the monsters health
        after the player has attacked.

        Args:
            attack_dmg: Player's base attack damage.
            weapon: Weapon that the player attacked with.
        """
        total_dmg = self.__calc_mod(weapon) * attack_dmg
        self.set_health(int(total_dmg))
		
    def __calc_mod(self, attack):
        """
        Method that calculates the attack modifier of the player
        based off of the weapon that was used to attack a specific monster.

        Args:
            attack: Weapon that the player used to attack.

        Returns:
            Returns the final attack modifier.   
        """
        if attack.name == "SourStraws":
            return attack.attack_mod * 2
        return attack.attack_mod


class Vampire(Monster):
    """
    Class that creates a Vampire monster.
    """

    def __init__(self, name="Vampire", health=50, attack_dmg=-5):
        """
        Constructor that calls the parent constructor and 
        initializes a Vampire object.

        Args:
            name: Name of the type of monster.
            health: Monsters health.
            attack_dmg: The amount of damage the monster attacks with.
        """
        super().__init__(name, health, attack_dmg)
        self.add_monster()

    def take_damage(self, attack_dmg, weapon):
        """
        Method that is responsible for updating the monsters health
        after the player has attacked.

        Args:
            attack_dmg: Player's base attack damage.
            weapon: Weapon that the player attacked with.
        """
        total_dmg = self.__calc_mod(weapon) * attack_dmg
        self.set_health(int(total_dmg))

    def __calc_mod(self, attack):
        """
        Method that calculates the attack modifier of the player
        based off of the weapon that was used to attack a specific monster.

        Args:
            attack: Weapon that the player used to attack.

        Returns:
            Returns the final attack modifier.   
        """
        if attack.name == "ChocolateBars":
            return 0
        return attack.attack_mod


class Ghoul(Monster):
    """
    Class that creates a Ghoul monster.
    """

    def __init__(self, name="Ghoul", health=80, attack_dmg=-7):
        """
        Constructor that calls the parent constructor and 
        initializes a Ghoul object.

        Args:
            name: Name of the type of monster.
            health: Monsters health.
            attack_dmg: The amount of damage the monster attacks with.
        """
        super().__init__(name, health, attack_dmg)
        self.add_monster()

    def take_damage(self, attack_dmg, weapon):
        """
        Method that is responsible for updating the monsters health
        after the player has attacked.

        Args:
            attack_dmg: Player's base attack damage.
            weapon: Weapon that the player attacked with.
        """
        total_dmg = self.__calc_mod(weapon) * attack_dmg
        self.set_health(int(total_dmg))

    def __calc_mod(self, attack):
        """
        Method that calculates the attack modifier of the player
        based off of the weapon that was used to attack a specific monster.

        Args:
            attack: Weapon that the player used to attack.

        Returns:
            Returns the final attack modifier.   
        """
        if attack.name == "NerdBombs":
            return attack.attack_mod * 5 
        return attack.attack_mod


class Werewolve(Monster):
    """
    Class that creates a Werewolve monster.
    """

    def __init__(self, name="Werewolve", health=60, attack_dmg=-12):
        """
        Constructor that calls the parent constructor and 
        initializes a Werewolve object.

        Args:
            name: Name of the type of monster.
            health: Monsters health.
            attack_dmg: The amount of damage the monster attacks with.
        """
        super().__init__(name, health, attack_dmg)
        self.add_monster()
        
    def take_damage(self, attack_dmg, weapon):
        """
        Method that is responsible for updating the monsters health
        after the player has attacked.

        Args:
            attack_dmg: Player's base attack damage.
            weapon: Weapon that the player attacked with.
        """
        total_dmg = self.__calc_mod(weapon) * attack_dmg
        self.set_health(int(total_dmg))

    def __calc_mod(self, attack):
        """
        Method that calculates the attack modifier of the player
        based off of the weapon that was used to attack a specific monster.

        Args:
            attack: Weapon that the player used to attack.

        Returns:
            Returns the final attack modifier.   
        """
        if attack.name == "ChocolateBars" or attack.name == "SourStraws":
            return 0
        return attack.attack_mod

