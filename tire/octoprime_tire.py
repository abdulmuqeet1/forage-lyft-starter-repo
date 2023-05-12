from tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, wear_level):
        self.__wear_level = wear_level

    def needs_service(self):
        return sum(self.__wear_level) >= 3