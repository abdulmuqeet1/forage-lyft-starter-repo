from battery import Battery
from utils import add_years

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date, battery_years_to_add=4):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.battery_years_to_add = battery_years_to_add

    def needs_service(self):
        date_battery_service = add_years(year=self.last_service_date + self.battery_years_to_add)
        if date_battery_service < self.current_date:
            return True
        else:
            return False