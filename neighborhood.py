from house import House

class Neighborhood():
    """
    Class that creates the map for the game.
    """
        
    def __init__(self):
        """
        Constructor that initializes the map and creates the houses,
        and neighbors so the player can move from house to house.
        """
        self.starting_h = House("Skywalker", self.skywalker_room())
        self.simpson_h = House("Simpson", self.simpson_room())
        self.mccallister_h = House("McCallister", self.mccallister_room())
        self.szalinski_h = House("Szalinski", self.szalinski_room())
        self.addams_h = House("Addams", self.addams_room())
        self.tanner_h = House("Tanner", self.tanner_room())
        self.taylor_h = House("Taylor", self.taylor_room())
        self.griswald_h = House("Griswald", self.griswald_room())
        self.player_h = House("Player", self.player_room())

        self.starting_h.add_neighbor("east", self.simpson_h)
        self.simpson_h.add_neighbor("west", self.starting_h)
        self.simpson_h.add_neighbor("south", self.mccallister_h)
        self.mccallister_h.add_neighbor("north", self.simpson_h)
        self.mccallister_h.add_neighbor("west", self.szalinski_h)
        self.mccallister_h.add_neighbor("east", self.addams_h)
        self.mccallister_h.add_neighbor("south", self.tanner_h)
        self.szalinski_h.add_neighbor("east", self.mccallister_h)
        self.addams_h.add_neighbor("west", self.mccallister_h)
        self.tanner_h.add_neighbor("north", self.mccallister_h)
        self.addams_h.add_neighbor("south", self.taylor_h)
        self.taylor_h.add_neighbor("north", self.addams_h)
        self.taylor_h.add_neighbor("west", self.tanner_h)
        self.tanner_h.add_neighbor("east", self.taylor_h)
        self.tanner_h.add_neighbor("south", self.griswald_h)
        self.griswald_h.add_neighbor("north", self.tanner_h)
        self.griswald_h.add_neighbor("west", self.player_h)
        self.player_h.add_neighbor("east", self.griswald_h)
           
    def skywalker_room(self):
        """
        Method that contains the description of the house.

        Returns:
            Returns the description of the house in a formatted string.
        """
        return ("You are at the Skywalker's house, nagivate your way home " 
                "battling monsters and turning\neveryone back to normal! "
                "To the east you will find the Simpson's house.")
        
    def simpson_room(self):
        """
        Method that contains the description of the house.

        Returns:
            Returns the description of the house in a formatted string.
        """
        return ("Towards the south you will find the McCallister's house.\n\n"
                "\"You can have all the money in the world, but there's one "
                "thing you\n will never have... a dinosaur.\"\n\t- Homer Simpson, "
                "The Simpsons")

    def mccallister_room(self):
        """
        Method that contains the description of the house.

        Returns:
            Returns the description of the house in a formatted string.
        """
        return ("There is a path that lies north to south and west to east.\n\n"
                "\"This is my house, I have to defend it.\"\n\t- Kevin McCallister"
                ", Home Alone")

    def szalinski_room(self):
        """
        Method that contains the description of the house.

        Returns:
            Returns the description of the house in a formatted string.
        """
        return ("Hmm.. seems like a dead end...\n\n"
                "\"We're now a quarter of an inch tall and sixty-four feet from"
                " the house. That's the\n equivalent of 3.2 miles, that's a long"
                " way, even for a man of science.\"\n\t- Nick Szalinski, Honey,"
                " I Shrunk the Kids")

    def addams_room(self):
        """
        Method that contains the description of the house.

        Returns:
            Returns the description of the house in a formatted string.
        """
        return ("To the south you will find the Taylor's house.\n\n"
                "\"And our credo, \'Sic gorgiamus allos subjectatos nunc\'"
                "-\'We gladly feast on those\n who would subdue us.\' Not just"
                " pretty words.\"\n\t- Morticia Addams, Addams Family")

    def taylor_room(self):
        """
        Method that contains the description of the house.

        Returns:
            Returns the description of the house in a formatted string.
        """
        return ("The Addams family lies north, while the Tanner family is "
                "west of you.\n\n"
                "\"That's Al \'I take my job seriously\' Borland....\"\n"
                "\t- Tim Taylor, Home Improvement")

    def tanner_room(self):
        """
        Method that contains the description of the house.

        Returns:
            Returns the description of the house in a formatted string.
        """
        return ("Towards the east you see the Taylor's house, and south "
                "of you is the Griswald's house.\n\n" 
                "\"Oh, Mylanta!\"\n\t– D.J. Tanner, Full House")

    def griswald_room(self):
        """
        Method that contains the description of the house.

        Returns:
            Returns the description of the house in a formatted string.
        """
        return ("To the west you see your house!\n\n"
                "\"I don't know to say, except it's Christmas and "
                "we're all in misery.\"\n\t- Clark Griswald, National Lampoon's "
                "Christmas Vacation")

    def player_room(self):
        """
        Method that contains the description of the house.

        Returns:
            Returns the description of the house in a formatted string.
        """
        return ("You have made it back to your house! To win you must defeat "
                "every monster\nand transform them back to normal!")

