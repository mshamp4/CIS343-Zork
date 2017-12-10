from house import House

class Neighborhood():
        
    def __init__(self):
        self.starting_h = House("Robinson", self.robinson_room())
        self.simpson_h = House("Simpson", self.simpson_room())
        self.ferguson_h = House("Ferguson", self.ferguson_room())
        self.chandler_h = House("Chandler", self.chandler_room())
        self.rodgers_h = House("Rodgers", self.rodgers_room())
        self.gonzalez_h = House("Gonzalez", self.gonzalez_room())
        self.jones_h = House("Jones", self.jones_room())
        self.anderson_h = House("Anderson", self.anderson_room())
        self.dewitt_h = House("DeWitt", self.dewitt_room())

        self.starting_h.add_neighbor("east", self.simpson_h)
        self.simpson_h.add_neighbor("west", self.starting_h)
        self.simpson_h.add_neighbor("south", self.ferguson_h)
        self.ferguson_h.add_neighbor("north", self.simpson_h)
        self.ferguson_h.add_neighbor("west", self.chandler_h)
        self.ferguson_h.add_neighbor("east", self.rodgers_h)
        self.ferguson_h.add_neighbor("south", self.gonzalez_h)
        self.chandler_h.add_neighbor("east", self.ferguson_h)
        self.rodgers_h.add_neighbor("west", self.ferguson_h)
        self.gonzalez_h.add_neighbor("north", self.ferguson_h)
        self.rodgers_h.add_neighbor("south", self.jones_h)
        self.jones_h.add_neighbor("north", self.rodgers_h)
        self.jones_h.add_neighbor("west", self.gonzalez_h)
        self.gonzalez_h.add_neighbor("east", self.jones_h)
        self.gonzalez_h.add_neighbor("south", self.anderson_h)
        self.anderson_h.add_neighbor("north", self.gonzalez_h)
        self.anderson_h.add_neighbor("west", self.dewitt_h)
        self.dewitt_h.add_neighbor("east", self.anderson_h)
           
    def robinson_room(self):
        return ("You are at your best friends house, "
                "the Robinsons, nagivate your way home battling "
                "monsters\nand turning everyone back to normal! To the east you "
                "will find the Simpsons house."
               )
        
    def simpson_room(self):
        return ("Simpson room")

    def ferguson_room(self):
        return ("Ferguson room")

    def chandler_room(self):
        return ("Chandler room")

    def rodgers_room(self):
        return ("Rodgers room")

    def jones_room(self):
        return ("Jones room")

    def gonzalez_room(self):
        return ("Gonzalez room")

    def anderson_room(self):
        return ("Anderson room")

    def dewitt_room(self):
        return ("DeWitt room")

