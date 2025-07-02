# table.py

class table:

    def __init__(self, data):
        self.data = data

    def display_headers():
        print("+------------+------------+------------+------------+------------+------------+")
        print("|    Name    |     Mass   |  Distance  | Satellites |    Moons   |   Radius   |")
        print("+------------+------------+------------+------------+------------+------------+")

    def display_body(self):
        for item in self.data:
            print("|", item.name.center(12," "), 
                  "|", item.mass.center(12," "), 
                  "|", item.distance.center(12," "), 
                  "|", item.satellites.center(12," "), 
                  "|", item.moons.center(12," "), 
                  "|", item.radius.center(12," "), "|")
            print("+------------+------------+------------+------------+------------+------------+")
        

    def display(self):
        self.display_headers()
        self.display_body()