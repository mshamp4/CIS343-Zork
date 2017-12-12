#!/usr/bin/env python

import os
import sys

from house import House
from player import Player
from neighborhood import Neighborhood
from monster import Monster
from weapon import Weapon

class Game:
    """
    Class that is responsible for running the game.
    In MVC design, this would be the view.
    """

    PLAYER_HEALTH = 130

    PLAYER_ATTACK_DMG = -20

    def __init__(self, world=None, current_loc=None, player=None):
        """
        Constructor that initializes a game object.

        Args:
            world: An instance of a neighborhood
            current_loc: Keeps track of the room that the player is in.
            player: The player.
        """
        self.clear_screen()
        self.zork_intro()
        self.print_commands()
        self._world = Neighborhood()
        self._current_loc = self.world.starting_h
        self._player = self.create_player()
        self._world.player_h._name = self._player._name
        self.clear_screen()
        self.intro_text()
        self._current_loc.print_description()

    @property
    def world(self):
        """
        Getter method for the world instance attribute.

        Returns:
            Returns an instance of a neighborhood.
        """
        return self._world

    @property
    def current_loc(self):
        """
        Getter method for the current location instance attribute.

        Returns:
            Returns the house that the player is in.
        """
        return self._current_loc

    @current_loc.setter
    def current_loc(self, new_loc):
        """
        Setter method for the current location instance attribute.

        Args:
            new_loc: The house that the player has moved too.
        """
        self._current_loc = new_loc

    @property
    def player(self):
        """
        Getter method for the player instance attribute.

        Returns:
            Returns the player object.
        """
        return self._player

    def create_player(self):
        """
        Method that creates a player with a name to make it more personalized.

        Returns:
            A player object with a name that has been entered by the user.

        Raises:
            EOFError: If the user presses ctrl-d.
            KeyboardInterrupt: If the user presses ctrl-c.
        """
        name = ""
        while(len(name) == 0):
            try:
                name = input("What is your name? ")
                name = name.strip()
            except EOFError:
                print("\nWhy did you stop me? :(")
                sys.exit(1)
            except KeyboardInterrupt:
                print("\nWhy did you stop me? :(")
                sys.exit(1)
        return Player(name, Game.PLAYER_HEALTH, Game.PLAYER_ATTACK_DMG)

    def clear_screen(self):
        """
        Method that clears the terminal screen so that gameplay looks nicer.
        """
        if not (os.name == 'nt'):
            os.system('clear')
        else:
            os.system('cls')

    def zork_intro(self):
        """
        Method that prints out the original Zork game message.
        """
        print(("ZORK I: The Great Underground Empire\n"
              "Copyright (c) 1981, 1982, 1983 Infocom, Inc. All rights reserved.\n"
              "ZORK is a registered trademark of Infocom, Inc.\n"
              "Revision 88 / Serial number 840726\n"
              ))

    def intro_text(self):
        """
        Method that prints out the objective of the game.
        """
        print(("%s, it's your job to save the day! Your neighborhood "
               "has been exposed to bad batches\nof candy and it has turned "
               "all of your neighbors into monsters!\n"
              ) % (self._player._name))

    def print_commands(self):
        """
        Method that prints out the list of avaiable commands the user can do.
        """
        print(("Command:\tShortcut:\tAction:\n"
              "north\t\tn\t\tMove north\n"
              "south\t\ts\t\tMove south\n"
              "east\t\te\t\tMove east\n"
              "west\t\tw\t\tMove west\n"
              "look\t\tl\t\tLooks around at current location\n"
              "inventory\ti\t\tShows contents of inventory\n"
              "take\t\tt\t\tPlaces item at current location in inventory\n"
              "diagnostic\t\t\tChecks current health condition\n"
              "attack [0-9]\ta [0-9]\t\tAttack all monsters with indexed item\n"
              "drop [0-9]\td [0-9]\t\tDrops item at specified inventory index\n"
              "help\t\t?\t\tDisplays this list of valid commands\n"
              "clear\t\t\t\tClear the terminal screen\n"
              "quit\t\tq\t\tQuit game\n"
              ))

    def check_loc(self, house):
        """
        Method that checks the houses location when a player wants to travel
        in the specified direction.

        Args:
            house: The house that the player attempts to traveled to.
        """
        if (house is None):
            print("you can't go that direction")
        else:
            self._current_loc = house
            if len(self._player.get_inventory()) < Weapon.MAX_WEAPONS and \
                   len(self._current_loc.get_weapon_list()) == 0:
                        self._current_loc.weapon_drop()
            self.clear_screen()
            self._current_loc.print_description()

    def end_text(self, condition, player):
        """
        Method that prints out the win/lose text of the game.

        Args:
            condition: Valid args "won" or "lost".
            player: The player that is currently playing the game.
        """
        if (condition == "won"):
            print(("Congratulations %s, you have defeated all of the monsters and "
                   "saved the neighborhood!") % (self._player._name, ))
        else:
            print(("%s, you have been defeated! Monsters "
                   "remaining: %i") % (self._player._name, 
                                       Monster._monster_count))

    def process_command(self, command):
        """
        Method that is responsible for taking user input and carrying out 
        game interactions.

        Args:
            command: A command that the user wants to make.
        """
        cmd_args = command.split()
        cmd_len = len(cmd_args)
        length = cmd_len == 2

        if (cmd_len < 1):
            return False

        if (command == "north" or command == "n"):
            self.check_loc(self._player.move("north", self._current_loc))
            return True

        if (command == "south" or command == "s"):
            self.check_loc(self._player.move("south", self._current_loc))
            return True

        if (command == "east" or command == "e"):
            self.check_loc(self._player.move("east", self._current_loc))
            return True

        if (command == "west" or command == "w"):
            self.check_loc(self._player.move("west", self._current_loc))
            return True

        if (command == "look" or command == "l"):
            self.clear_screen()
            self._current_loc.print_description()
            return True

        if (command == "inventory" or command == "i"):
            self._player.print_inventory()
            return True

        if (command == "take" or command == "t"):
            num = self._player.take(self._current_loc)
            if (num == 0):
               print("No weapons available to take!")
            elif (num == 10):
               print("Inventory full")
            else:
               self.clear_screen()
               self._current_loc.print_description()
            return True

        if (command == "diagnostic"):
            print("Health:", self.player._health)
            return True

        if (length and (cmd_args[0] == "attack" or cmd_args[0] == "a") and
                cmd_args[1].isdigit() and int(cmd_args[1]) <= 9):

            if (len(self._current_loc._monsters) == 0):
                print("No monsters available to attack!")
                return True

            if (int(cmd_args[1]) >= len(self._player.get_inventory())):
                print("Weapon not in inventory!")
                return True

            dmg = self._player.attack(self._player.get_inventory()[int(cmd_args[1])],
                                      self._current_loc._monsters)
            self.clear_screen()
            self._current_loc.print_description()
            print("Damge taken:", dmg)
            print("Health:", self._player.get_health())
            return True

        if (length and (cmd_args[0] == "drop" or cmd_args[0] == "d") and
                cmd_args[1].isdigit() and int(cmd_args[1]) <= 9):
            if not (self._player.drop_item(int(cmd_args[1]), self._current_loc)):
                print("Weapon not in inventory")
                return True
            self.clear_screen()
            self._current_loc.print_description()
            return True

        if (command == "help" or command == "?"):
            self.print_commands()
            return True

        if (command == "clear"):
            game.clear_screen()
            return True

        if (command == "quit" or command == "q"):
            print("Goodbye", self._player._name)
            sys.exit()

        return False

if __name__ == "__main__":
    """
    Main method that runs the game loop.
    The game only stops if the player has died or if the player has won the game.

    Raises:
        EOFError: If the user presses ctrl-d.
        KeyboardInterrupt: If the user presses ctrl-c.
    """

    game = Game()
   
    while(game._player.is_alive()):
        if (game._player.win_condition()):
            game.end_text("won", game._player)
            sys.exit()

        try:
            command = input()
            if not (game.process_command(command.strip().lower())):
                print("invalid command")
        except EOFError:
                print("\nWhy did you stop me? :(")
                sys.exit(1)
        except KeyboardInterrupt:
                print("\nWhy did you stop me? :(")
                sys.exit(1)

    game.end_text("lost", game._player)
    sys.exit()

