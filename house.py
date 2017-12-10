from random import randint

from observer.observer import Observer
from observable.observable import Observable
from weapon import Weapon
from monster import Monster, Person, Zombie, Vampire, Ghoul, Werewolve

class House(Observer, Observable):

    def __init__(self, name, description):
        """A class to store house information."""
        Observable.__init__(self)
        self._name = name
        self._description = description
        self._weapons = []
        self._directions = {}
        self._monsters = self.spawn_monsters()

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def spawn_monsters(self):
        num_monsters = randint(0, 10)
        monsters = []
        for i in range(num_monsters):
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
            monsters.append(monster)
            monster.add_observer(self)
        return monsters
        
    def add_weapon(self, weapon):
        if not weapon in self._weapons:
            self._weapons.append(weapon)

    def remove_weapon(self, weapon):
        if weapon in self._weapons:
            self._weapons.remove(weapon)

    def get_weapon_list(self):
        return self._weapons

    def get_monster_list(self):
        return self._monsters

    def print_description(self):
        print(self._description)
        self.print_house_interactions()

    def print_house_interactions(self):
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
                    print_str += "\t\t"
                if (i < w_len):
                    print_str += weapon_str[i] + "\t"
                if (i < m_len):
                    if (i >= w_len and (not w_len == 0)):
                        print_str += "\t\t" + monster_str[i]
                    else:
                        print_str += monster_str[i]
            print(print_str)
               
    def weapon_drop(self):
        num = randint(1, 2)
        for x in range(num):
            self._weapons.append(Weapon(*Weapon.WEAPON_VALUES[randint(1,  3)], 0))
       
    def max_weapons(self):
        return Weapon.MAX_WEAPONS

    def add_neighbor(self, direction, house):
        self._directions[direction] = house

    def get_neighbor(self, direction):
        return self._directions.get(direction, None)    

    def update(self, observable, msg):
        observable.remove_observer(self)
        self.remove_monster()
        person = Person()
        index = self._monsters.index(observable)
        self._monsters.remove(observable)
        self._monsters.insert(index, person)
        self.update_observers("died")

