from batteries.battery import Battery
from utils import add_years


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date, battery_years_to_add=2):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.battery_years_to_add = battery_years_to_add

    def needs_service(self) -> bool:
        date_battery_service = add_years(year=last_service_date + self.battery_years_to_add)
        return self.current_date > date_battery_service