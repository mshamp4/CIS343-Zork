# -*- coding: utf-8 -*-

class Weapon():

    MAX_WEAPONS = 10

    WEAPON_VALUES = {0:("HersheyKisses", 1.0, 1000),
                     1:("SourStraws", 1.5, 2),
                     2:("ChocolateBars", 2.1, 4),
                     3:("NerdBombs", 4.2, 1)}

    def __init__(self, name="Default", attack_mod=0.0, ammo=0, command=0):
        self._name = name
        self._attack_mod = attack_mod
        self._ammo = ammo
        self._command = command

    @property
    def name(self):
        return self._name

    @property
    def attack_mod(self):
        return self._attack_mod

    def get_ammo(self):
        return self._ammo

    def set_ammo(self, value):
        self._ammo -= value

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value

    def __str__(self):
        if (self._name == "HersheyKisses"):
            return ("%s %s\t\t%s\t\u221E") % (self._command, self._name, 
                                              self._attack_mod)

        return ("%s %s\t\t%s\t%s") % (self._command, self._name, 
                                      self._attack_mod, self._ammo)

