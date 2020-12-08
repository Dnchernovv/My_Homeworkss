class Road:
    def __init__(self,length,width):
        self._length = length
        self._width = width

    def formula(self):
        asphalt = (self._length*self._width*5*25)/1000
        return asphalt

my_road = Road(20,5000)
print(my_road.formula())

