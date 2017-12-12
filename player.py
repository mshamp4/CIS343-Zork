from random import randint

from observable.observable import Observable
from monster import Monster, Person, Zombie, Vampire, Ghoul, Werewolve
from weapon import Weapon
from house import House

class Player(Observable):
    """
    Class that creates a player object.

    Player inherits from Observable because when the player attacks 
    the monsters, if a monster dies it calls the house's update method.
    """
    #TODO: In the future I should make this class a singleton
    #so that I can ensure this class is only called once.

    _inventory = []

    def __init__(self, name="Player", health=130, attack_dmg=-20):
        """
        Constructor that intializes a player object.

        Args:
            name: The players name.
            health: Players health.
            attack_dmg: The amount of damage the player attacks with.
        """
        super().__init__()
        self._name = name
        self._health = health
        self._attack_dmg = attack_dmg
        self._create_inventory()

    @property
    def name(self):
        """
        Getter method for the name instance attribute.

        Returns:
            Returns the name of the player.
        """
        return self._name
    
    #Could not decorate this as well. Setters replace the value.
    def get_health(self):
        """
        Getter method for the health instance attribute.

        Returns:
            Returns the health of the player.
        """
        return self._health

    def set_health(self, value):
        """
        Setter method for the health instance attribute.

        Args:
            value: The amount of total damage taken from all of the monsters in
                   the current house the player is in.
        """
        self._health += value

    @property
    def attack_dmg(self):
        """
        Getter method for the attack damage instance attribute.

        Returns:
            Returns the attack damage of the player.
        """
        return self._attack_dmg

    def is_alive(self):
        """
        Method that checks if the player is still alive.

        Returns:
            Returns True if the player is still alive else False.
        """
        return self._health > 0

    def _create_inventory(self):
        """
        Method that creates the inventory for the player.

        In the weapon class there is a tuple that contains the
        proper values for each weapon.
        """
        Player._inventory.append(Weapon(*Weapon.WEAPON_VALUES[0], 0))

        for assign_cmd in range(1, Weapon.MAX_WEAPONS):
            num = randint(1, 3)
            Player._inventory.append(Weapon(*Weapon.WEAPON_VALUES[num],
                                            assign_cmd))
    
    def get_inventory(self):
        """
        Getter method that returns the players inventory.

        Returns:
            Returns a mutable ordered sequence of weapon objects.
        """
        return Player._inventory

    def _update_inventory(self):
        """
        Method that gets called each time the player attacks a house.

        If a weapon's ammo is 0 it removes it from the inventory.
        """
        for weapon in Player._inventory:
            if weapon._ammo == 0:
                Player._inventory.remove(weapon)
                self.rebind_commands()

    def print_inventory(self):
        """
        Method that prints the players inventory along with the 
        stats for each weapon.
        """
        print("\t%s's Inventory" % (self._name))
        print("  Weapon:\t\tMod:\tAmmo:")
        for weapon in Player._inventory:
            print(weapon)

    def drop_item(self, index, house):
        """
        Method that adds a weapon to the house's mutable list.

        Args:
            index: An integer (0-9) that corresponds to a specific weapon.
            house: The house that the player is trying to drop a weapon in.

        Returns:
            Returns True if a weapon has been dropped else returns False if
            there is no weapon in the player's inventory.
        """
        for weapon in Player._inventory:
            if weapon.command == index:
                house.add_weapon(weapon)
                Player._inventory.remove(weapon)
                self.rebind_commands()
                return True
        return False

    def take(self, current_loc):
        """
        Method that picks up a weapon from the house's mutable list of weapons.

        Args:
            current_loc: The current house that the player is in.

        Returns:
            Returns 1 if the player took the item, else returns 0 if the house
            contains no weapons or returns 10 if the players inventory is full.
        """
        room_weapons = current_loc.get_weapon_list()
        if (len(room_weapons) == 0):
            return 0

        if (len(Player._inventory) < Weapon.MAX_WEAPONS):
            Player._inventory.append(room_weapons[0])
            self.rebind_commands()
            current_loc.remove_weapon(room_weapons[0])
            return 1
        else:
            return 10

    def rebind_commands(self):
        """
        Method that assigns an integer (0-9) to a specific weapon so the
        player can attack with it.
        """
        count = 0
        for weapon in self.get_inventory():
            weapon.command = count
            count += 1

    def attack(self, weapon, monster):
        """
        Method that attacks all of the monsters in the house at once.
        When the player attacks, the monsters attack back as well. If a 
        monster dies it calls the house's update method to remove it from the
        game.

        Args:
            weapon: Weapon used to attack the monsters.
            monster: List of monsters that are in the current house.

        Returns:
            Returns the combined total damage taken by each monster.
        """
        dmg_taken = 0
        num_person = 0
        for enemy in monster:
            dmg_taken += enemy.attack_dmg
            if not isinstance(enemy, Person):
                enemy.take_damage(self._attack_dmg, weapon)
                weapon.set_ammo(1)
                self._update_inventory()
                if not enemy.is_alive():
                    Observable.update_observers(enemy)
            else:
                num_person += 1        
        if num_person == len(monster):
            return 0
        self.set_health(dmg_taken)
        return dmg_taken

    def move(self, direction, current_loc):
        """
        Method that moves the player from house to house.

        Args:
            direction: Valid args "north", "south", "west", or "east".
            current_loc: The current house the player is in.

        Returns:
            Returns a house if there is one, else returns None.
        """
        return current_loc.get_neighbor(direction)

    def win_condition(self):
        """
        Method that checks to see if the player has won the game.
        The game is over when the player is still alive and has killed
        all of the monsters.

        Returns:
            Returns True if the player won, else returns False.
        """
        return (self.is_alive() and Monster._monster_count == 0)

