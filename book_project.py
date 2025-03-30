# Problem Statement: Travel Booking System
# You are developing a travel booking system where users can book flights. The system should allow:
#
# A user to book a flight ticket by specifying the destination and departure city (required parameters).
# Multiple travelers can be included in the booking (variable arguments *args).
# Additional services (like meal preference, extra baggage, seat selection, etc.) can be provided as optional details (keyword arguments **kwargs).
# Task:
# Write a function book_flight(departure, destination, *travelers, **extras).
# The function should display the departure city, destination, travelers, and additional services.
# Test the function with different arguments.
# Modify the function to calculate the total cost:
#
# Each traveler costs $500.
# Extra baggage costs $50.
# Meal costs $20 per traveler.
# Example Input & Expected Output
# Function Call
# book_flight("New York", "Paris", "Alice", "Bob", meal="Vegetarian", seat="Window", extra_baggage=True)
#
# Flight booked from New York to Paris.
#
# Travelers:
# - Alice
# - Bob
# Additional Services:
# - Meal: Vegetarian
# - Seat: Window
# - Extra Baggage: True
#
# Booking confirmed!
def book_flight(departure, destination, *travelers, **extras):
    traveler_cost = len(travelers) * 500
    print(f"Flight booked from {departure} to {destination}")
    print("\nTravelers:")
    for people in travelers:
        print("- ", people)
    if extras:
        print("Additional Services")
        for key, value in extras.items():
            print(key, ": ", value)
        if "meal_service" in extras:
            meal_cost = len(travelers)*20
            traveler_cost+=meal_cost
        if "extra_baggage" in extras and extras["extra_baggage"]:
            traveler_cost+=50
    print(f"the total cost is: {traveler_cost}")
    print("\nBooking confirmed!")



book_flight("New York", "Paris", "Alice", "Bob", meal_service = "vegetarian", seat = "window", extra_baggage = True)