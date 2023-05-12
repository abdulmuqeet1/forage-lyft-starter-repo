from tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear_level):
        self.__wear_level = wear_level

    def needs_service(self):
        return any(wear >= 0.9 for wear in self.__wear_level)