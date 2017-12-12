# -*- coding: utf-8 -*-

class Weapon():
    """
    Class that creates a weapon object.
    """

    MAX_WEAPONS = 10

    WEAPON_VALUES = {0:("HersheyKisses", 1.0, 1000),
                     1:("SourStraws", 1.5, 2),
                     2:("ChocolateBars", 2.1, 4),
                     3:("NerdBombs", 4.2, 1)}

    def __init__(self, name="Default", attack_mod=0.0, ammo=0, command=0):
        """
        Constructor that initializes a weapon object.

        Args:
            name: Name of the weapon.
            attack_mod: How much additional damage the weapon does.
            ammo: The amount of times the player can use this weapon.
            command: How the player specifies which weapon to attack with.
        """
        self._name = name
        self._attack_mod = attack_mod
        self._ammo = ammo
        self._command = command

    @property
    def name(self):
        """
        Getter method for the name instance attribute.

        Returns:
            Returns the name of the weapon.
        """
        return self._name

    @property
    def attack_mod(self):
        """
        Getter method for the attack modifier instance attribute.

        Returns:
            Returns the amount of additional damage the weapon will do.
        """
        return self._attack_mod

    def get_ammo(self):
        """
        Getter method for the ammo instance attribute.

        Returns:
            Returns the amount of ammo the weapon has.
        """
        return self._ammo

    def set_ammo(self, value):
        """
        Setter method for the ammo instance attribute.

        Args:
            value: It will always be one, when the player attacks with a weapon
                   this method is called.
        """
        self._ammo -= value

    @property
    def command(self):
        """
        Getter method for the command instance attribute.

        Returns:
            Returns the command (0-9) that the player can use to attack with.
        """
        return self._command

    @command.setter
    def command(self, value):
        """
        Setter method for the command instance attribute.

        Args:
            value: An integer (0-9) that is used so the player can attack with it.
        """
        self._command = value

    def __str__(self):
        """
        Method that is the toString for the weapon class. If the weapon is 
        HersheyKisses, a UTF-8 encoding of an infinity symbol is used.
        """
        if (self._name == "HersheyKisses"):
            return ("%s %s\t\t%s\t\u221E") % (self._command, self._name, 
                                              self._attack_mod)

        return ("%s %s\t\t%s\t%s") % (self._command, self._name, 
                                      self._attack_mod, self._ammo)

