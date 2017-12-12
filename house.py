from random import randint

from observer.observer import Observer
from observable.observable import Observable
from weapon import Weapon
from monster import Monster, Person, Zombie, Vampire, Ghoul, Werewolve

class House(Observer, Observable):
    """
    Class that creates a house object that observes monsters.
    
    A house object contains a name, description, two mutable ordered sequences
    that contain weapon and house objects, as well as a dictionary of directions.
    """

    #Game became too op and I had to reduce the number of monsters
    #that spawn in each room.
    MONSTERS = 8

    def __init__(self, name, description):
        """
        Constructor that initializes a house object.

        Args:
            name: Last name of a family.
            description: Storyline that describes the house and family.
        """
        Observable.__init__(self)
        self._name = name
        self._description = description
        self._weapons = []
        self._directions = {}
        self._monsters = self.spawn_monsters()

    @property
    def name(self):
        """
        Getter method for the name instance attribute.
        
        Returns:
            Returns the name of the house.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Setter method for the name instance attribute.
        
        Args:
            value: Last name of a family.
        """
        self._name = value

    @property
    def description(self):
        """
        Getter method for the description instance attribute.
        
        Return:
            Returns the description of the house. 
        """
        return self._description

    def spawn_monsters(self):
        """
        Method that creates the monsters for each house and also adds
        the house as an observer to each monster.

        Returns:
            Returns a list of random monsters that vary in length 
            from 0 to House.MONSTERS.
        """
        num = randint(0, House.MONSTERS)
        monster_list = []
        for i in range(num):
            rand = randint(1, 5)
            monster = None
            if (rand == 1):
                monster = Person()
            elif (rand == 2):
                monster = Zombie()
            elif (rand == 3):
                monster = Vampire()
            elif (rand == 4):
                monster = Ghoul()
            elif (rand == 5):
                monster = Werewolve()
            monster_list.append(monster)
            monster.add_observer(self)
        return monster_list
        
    def add_weapon(self, weapon):
        """
        Method that adds a weapon to the house's mutable list of weapons.
        
        Args:
            weapon: The weapon that is dropped by the player.
        """
        if not weapon in self._weapons:
            self._weapons.append(weapon)

    def remove_weapon(self, weapon):
        """
        Method that removes a weapon from the house's mutable list of weapons.
        
        Args:
            weapon: The weapon that the player picks up from the house.
        """
        if weapon in self._weapons:
            self._weapons.remove(weapon)

    def get_weapon_list(self):
        """
        Method that returns a mutable list of weapons that the house is holding.

        Returns:
            Returns a list of weapons.
        """
        return self._weapons

    def get_monster_list(self):
        """
        Method that returns a mutable list of monsters that the house is holding.

        Returns:
            Returns a list of monsters.
        """
        return self._monsters

    def print_description(self):
        """
        Method that prints the storyline of each house as well as the monsters 
        and weapons that it currently has.

        """
        print("%s's house" % (self._name))
        print(self._description)
        self.print_house_interactions()

    def print_house_interactions(self):
        """
        Method that is only responsible for printing the monsters and weapons of
        each house.

        """
        print("\nHouse weapons:\tMonsters:\tHealth:")
        weapon_str = []
        monster_str = []
        for weapon in self._weapons:
            weapon_str.append(weapon._name)

        for mon in self._monsters:
            if isinstance(mon, Werewolve):
                monster_str.append(mon._name + "\t" + str(mon._health))
            else:
                monster_str.append(mon._name + "\t\t" + str(mon._health))
 
        w_len = len(weapon_str)
        m_len = len(monster_str)
        max_len = w_len if (w_len > m_len) else m_len

        for i in range(max_len):
            print_str = ""
            if (w_len == 0):
                print_str = "\t\t"
            if (i < w_len):
                print_str = weapon_str[i] + "\t"
            if (i < m_len):
                if (i >= w_len and (not w_len == 0)):
                    print_str += "\t\t" + monster_str[i]
                else:
                    print_str += monster_str[i]
            print(print_str)
               
    def weapon_drop(self):
        """
        Method that randomly drops 1-2 weapons in each house the 
        player visits as long as the player's inventory is not full 
        and the house does not contain any weapons already.

        """
        num = randint(1, 2)
        for x in range(num):
            self._weapons.append(Weapon(*Weapon.WEAPON_VALUES[randint(1,  3)], 0))
       
    def add_neighbor(self, direction, house):
        """
        Method that adds a house object (value) and associates a direction (key)
        with it to its dictionary.
        
        Args:
            direction: The key to be added to the house's dictionary.
            house: The value to be added to the house's dictionary.
        """
        self._directions[direction] = house

    def get_neighbor(self, direction):
        """
        Method that gets the house's neighbor.

        Args:
            direction: Valid args "north", "south", "west", "east".

        Returns:
            Returns a house object if there is one else it returns None.
        """
        return self._directions.get(direction, None)    

    def update(self, observable):
        """
        Method that removes the house (observer) from the monster and 
        updates the house with a person.

        Args:
            observable: Monster object that has died (health <= 0).
        """
        observable.remove_monster()
        observable.remove_observer(self)
        person = Person()
        index = self._monsters.index(observable)
        self._monsters.remove(observable)
        self._monsters.insert(index, person)
        person.add_observer(self)

