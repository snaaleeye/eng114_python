class Aircraft:

    def __init__(self, limit = 150):
        self.passengers = [120]
        self.aircraft_limit = 150
        self.is_aircraft_full = False

    def is_aircraft_full(self):
        if self.passengers >= self.aircraft_limit:
            print("This aircraft has vacant seats")
        else:
            print("This aircraft is full")

    def add_passenger(self):
        if len(self.passengers) >= self.aircraft_limit:
            self.passengers.append()
        else:
            self.is_aircraft_full = True

    def passenger_left(self):
        self.passengers.pop()

    def aircraft_status(self):
        if self.is_aircraft_full:
            print("This aircraft is full")
        else:
             print("This aircraft has vacant seats")

BA = Aircraft()
BA.aircraft_status()

name aircraft
