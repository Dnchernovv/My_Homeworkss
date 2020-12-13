from abc import ABC,abstractmethod
class Clothes(ABC):
    def __init__(self,material):
        self.material = material
    @abstractmethod
    def calculate_material(self):
        pass
class Coat(Clothes):
    @property
    def calculate_material(self):
        return self.material/6.5 + 0.5
class Costume(Clothes):
    @property
    def calculate_material(self):
        return self.material * 2 + 0.3

costume = Costume(10)
coat = Coat(20)
print(costume.calculate_material)
print(coat.calculate_material)