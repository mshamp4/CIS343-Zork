from random import randint

from observable.observable import Observable
from monster import Monster, Person, Zombie, Vampire, Ghoul, Werewolve
from weapon import Weapon
from house import House

class Player(Observable):

    _inventory = []

    def __init__(self, name="Player", health=100, attack_dmg=-15):
        self._name = name
        self._health = health
        self._attack_dmg = attack_dmg
        self._create_inventory()

    @property
    def name(self):
        return self._name
    
    def get_health(self):
        return self._health

    def set_health(self, value):
        self._health += value

    @property
    def attack_dmg(self):
        return self._attack_dmg

    def is_alive(self):
        return self._health > 0

    def _create_inventory(self):
        Player._inventory.append(Weapon(*Weapon.WEAPON_VALUES[0], 0))

        for assign_cmd in range(1, 10):
            num = randint(1, 3)
            Player._inventory.append(Weapon(*Weapon.WEAPON_VALUES[num],
                                            assign_cmd))
    
    def get_inventory(self):
        return Player._inventory

    def _update_inventory(self):
        for weapon in Player._inventory:
            if weapon._ammo == 0:
                Player._inventory.remove(weapon)
                self.rebind_commands()

    def print_inventory(self):
        print("\t%s's Inventory" % (self._name))
        print("  Weapon:\t\tMod:\tAmmo:")
        for weapon in Player._inventory:
            print(weapon)

    def drop_item(self, index, house):
        for weapon in Player._inventory:
            if weapon.command == index:
                house.add_weapon(weapon)
                Player._inventory.remove(weapon)
                self.rebind_commands()
                return True
        return False

    def take(self, current_loc):
        room_weapons = current_loc.get_weapon_list()
        if (len(room_weapons) == 0):
            print("No weapons available to take!")

        if (len(Player._inventory) < Weapon.MAX_WEAPONS):
            Player._inventory.append(room_weapons[0])
            self.rebind_commands()
            current_loc.remove_weapon(room_weapons[0])
        else:
            print("Inventory full")

    def rebind_commands(self):
        count = 0
        for weapon in self.get_inventory():
            weapon.command = count
            count += 1

    def attack(self, weapon, monster):
        dmg_taken = 0
        for enemy in monster:
            dmg_taken += enemy.attack_dmg
            if not isinstance(enemy, Person):
                enemy.take_damage(self._attack_dmg, weapon)
                self.set_health(dmg_taken)
                weapon.set_ammo(1)
                self._update_inventory()
                self.update_observers(monster)
        return dmg_taken

    def move(self, direction, current_loc):
        return current_loc.get_neighbor(direction)

    def win_condition(self):
        return (self.is_alive() and Monster.monsters_remaining == 0)

