import time
from itertools import cycle
class TrafficLight:
    def __init__(self):
        self._colour = ['Red', 'Orange', 'Green']
    def running(self):
        for i in cycle(self._colour):
            if self._colour.index(i) == 0:
                time.sleep(5)
            elif self._colour.index(i) == 1:
                time.sleep(7)
            elif self._colour.index(i) == 2:
                time.sleep(5)
            print(i)
traf_l = TrafficLight()
traf_l.running()