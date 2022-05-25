# Create own hierarchy of inheritance
# User story - 1 - As a checkin assistant, I want to be able to list all flights_trip available, so that I can sell tickes or check passanger list on specicic flight_trip

# User story - 2 - As a checkin assistant, I should be able to see the origin, destination and date of any flight

# User story - 3 - As a checkin assistant, I want to be able to list all passangers and their passaport number for any fligth_trip

# User story - 4 - As a checkin assistant, I want to be able to register passangers with first name, last name and passport number

# User story - 5 - As a checkin assistant, I should be able to register passangers to specific flight_trips

# EXTRA # User story - 6 - As a checkin assistant, I want to be able to export a flight_trip's passanger_list to a txt or csv file

# EXTRA # User story - 7 - As a checkin assistant, I want to be able to export a flight_trip's passanger_list to a txt or csv file


# # Origin, Destination and Date of any flight
# # List all passenger names and passport numbers
# # Able to register all passengers with first name Last name passport number
# # Able to add specific passengers to specific flights.

# departures_today = ["JFK to LHR", "LHR to JFK", "LHR to CDG", "CDG to LHR", "LHR to DUB", "DUB to JFK"]
#
# departures_future = ["HND to LHR", "LHR to PEK","ICN to LHR", "IST to DXB","DXB to LHR", "OSL to LHR"]
#
# print("Press 1 to view all flights departing today")
# print("Press 2 to view all future flight departures")
# while True:
#     choice = input("Please select")
#     if choice in ('1', '2'):
#
#         if choice == '1':
#             print(f"Available flights today are {departures_today}")
#
#         elif choice == '2':
#             print(f"Future available flights are {departures_future}")
#
#         next_booking = input("Anything else? (yes/no): ")
#         if next_booking == "no":
#             break
#
#     else:
#         print("Invalid Input")