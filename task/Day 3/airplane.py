from aircraft import Aircraft

class Airplane(Aircraft):
    def __init__(self):
        super().__init__()
        self.airplane = ["British Airways"]

    departures_today = ["JFK to LHR", "LHR to JFK", "LHR to CDG", "CDG to LHR", "LHR to DUB", "DUB to JFK"]

    departures_future = ["HND to LHR", "LHR to PEK", "ICN to LHR", "IST to DXB", "DXB to LHR", "OSL to LHR"]

    print("Press 1 to view all flights departing today")
    print("Press 2 to view all future flight departures")
    while True:
        choice = input("Please select")
        if choice in ('1', '2'):

            if choice == '1':
                print(f"Available flights today are {departures_today}")

            elif choice == '2':
                print(f"Future available flights are {departures_future}")

            next_booking = input("Anything else? (yes/no): ")
            if next_booking == "no":
                break

        else:
            print("Invalid Input")