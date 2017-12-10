from random import randint

from observer.observer import Observer
from observable.observable import Observable

class Monster(Observable):
	
    _monster_count = 0

    def __init__(self, name, health, attack_dmg):
        super().__init__()
        self._name = name
        self._health = health	
        self._attack_dmg = attack_dmg

    @property
    def name(self):
        return self._name
	
    def get_health(self):
        return self._health

    def set_health(self, damage):
        self._health += damage

    @property
    def attack_dmg(self):
        return self._attack_dmg

    def add_monster(self):
        Monster._monster_count += 1

    def remove_monster(self):
        Monster._monster_count -= 1

    def monsters_remaining(self):
        return Monster._monster_count

    def is_alive(self):
        if self._health > 0:
           self.update_observers("died")
        
class Person(Monster):
    def __init__(self, name="Person", health=100, attack_dmg=2):
        super().__init__(name, health, attack_dmg)
		
class Zombie(Monster):
    def __init__(self, name="Zombie", health=50, attack_dmg=-1):
        super().__init__(name, health, attack_dmg)
        super(Zombie, self).add_monster()

    def take_damage(self, attack_dmg, weapon):
        total_dmg = self.__calc_mod(weapon) * attack_dmg
        self.set_health(int(total_dmg))
		
    def __calc_mod(self, attack):
        if attack.name == "SourStraws":
            return attack.attack_mod * 2
        return attack.attack_mod

class Vampire(Monster):
    def __init__(self, name="Vampire", health=100, attack_dmg=-5):
        super().__init__(name, health, attack_dmg)
        super(Vampire, self).add_monster()

    def take_damage(self, attack_dmg, weapon):
        total_dmg = self.__calc_mod(weapon) * attack_dmg
        self.set_health(int(total_dmg))

    def __calc_mod(self, attack):
        if attack.name == "ChocolateBars":
            return 0
        return attack.attack_mod

class Ghoul(Monster):
    def __init__(self, name="Ghoul", health=60, attack_dmg=-7):
        super().__init__(name, health, attack_dmg)
        super(Ghoul, self).add_monster()

    def take_damage(self, attack_dmg, weapon):
        total_dmg = self.__calc_mod(weapon) * attack_dmg
        self.set_health(int(total_dmg))

    def __calc_mod(self, attack):
        if attack.name == "NerdBombs":
            return attack.attack_mod * 5 
        return attack.attack_mod

class Werewolve(Monster):
    def __init__(self):
        super().__init__(name="Werewolve", health=150, attack_dmg=-12)
        super(Werewolve, self).add_monster()
        
    def take_damage(self, attack_dmg, weapon):
        total_dmg = self.__calc_mod(weapon) * attack_dmg
        self.set_health(int(total_dmg))

    def __calc_mod(self, attack):
        if attack.name == "ChocolateBars" or attack.name == "SourStraws":
            return 0
        return attack.attack_mod

