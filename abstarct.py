from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofSides(self):
        pass

class Triangle(Polygon):

    def noofSides(self):
        print("I have a three sides:")

class Pentagoan(Polygon):
    def noofSides(self):
        print("I have a five sides:")

class Hexagon(Polygon):
    def noofSides(self):
        print("I have a six sides:")

R=Triangle()
R.noofSides()

R=Pentagoan()
R.noofSides()

R=Hexagon()
R.noofSides()
