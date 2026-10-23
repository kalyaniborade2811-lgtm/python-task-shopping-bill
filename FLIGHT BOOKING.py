from abc import ABC, abstractmethod


# Abstract Base Class
class Passenger(ABC):
    def _init_(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass


# Inheritance
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


class StudentPassenger(Passenger):
    def get_discount(self):
        return 10


# Flight Class
class Flight:
    def _init_(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self._available_seats = seats
        self.base_fare = fare

    def display_flight(self):
        print(
            self.code, "|", self.airline, "|",
            self.source, "to", self.destination,
            "| Seats:", self._available_seats,
            "| Fare: Rs.", self.base_fare
        )

    def get_available_seats(self):
        return self._available_seats

    def book_seats(self, tickets):
        if tickets <= self._available_seats:
            self._available_seats -= tickets
            return True
        return False


# Booking Class
class Booking:
    def _init_(self, booking_id, flight, passenger,
                 passenger_type, tickets, subtotal,
                 discount, total):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.passenger_type = passenger_type
        self.tickets = tickets
        self.subtotal = subtotal
        self.discount = discount
        self.total = total

    def display_summary(self):
        print("\n===== BOOKING SUMMARY =====")
        print("Booking ID:", self.booking_id)
        print("Flight Code:", self.flight.code)
        print("Airline:", self.flight.airline)
        print("Route:", self.flight.source, "to",
              self.flight.destination)
        print("Passenger Name:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Passenger Type:", self.passenger_type)
        print("Tickets:", self.tickets)
        print("Base Fare per Ticket: Rs.", self.flight.base_fare)
        print("Subtotal: Rs.", self.subtotal)
        print("Discount: Rs.", self.discount)
        print("Final Amount: Rs.", self.total)
        print("===========================\n")


# Main Flight Booking System
class FlightBookingSystem:
    def _init_(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB102", "Kiran Air", "Mumbai", "Bengaluru", 25, 3500),
            Flight("PN103", "Kiran Air", "Pune", "Hyderabad", 15, 3000)
        ]

        self.bookings = []
        self.booking_counter = 1001

    def display_flights(self):
        print("\n========== AVAILABLE FLIGHTS ==========")
        for flight in self.flights:
            flight.display_flight()
        print("=======================================\n")

    def find_flight(self, code):
        for flight in self.flights:
            if flight.code.lower() == code.lower():
                return flight
        return None

    def validate_booking(self, flight, name, age, tickets):
        if flight is None:
            print("Error: Invalid flight code.")
            return False

        if not name.strip():
            print("Error: Passenger name cannot be blank.")
            return False

        if age <= 0:
            print("Error: Age must be greater than zero.")
            return False

        if tickets <= 0:
            print("Error: Tickets must be greater than zero.")
            return False

        if tickets > flight.get_available_seats():
            print("Booking failed: Not enough seats available.")
            return False

        return True

    def book_flight(self):
        try:
            code = input("Enter flight code: ").strip()
            flight = self.find_flight(code)

            name = input("Enter passenger name: ").strip()
            age = int(input("Enter age: "))

            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()

            tickets = int(input("Enter number of tickets: "))

            if passenger_type not in ["regular", "student"]:
                print("Error: Enter Regular or Student.")
                return

            if not self.validate_booking(
                flight, name, age, tickets
            ):
                return

            if passenger_type == "student":
                passenger = StudentPassenger(name, age)
                passenger_label = "Student"
            else:
                passenger = RegularPassenger(name, age)
                passenger_label = "Regular"

            # Polymorphism: same method, different discounts
            subtotal = flight.base_fare * tickets
            discount = subtotal * passenger.get_discount() / 100
            total = subtotal - discount

            # Update seats only after validation succeeds
            flight.book_seats(tickets)

            booking = Booking(
                "BK" + str(self.booking_counter),
                flight,
                passenger,
                passenger_label,
                tickets,
                subtotal,
                discount,
                total
            )

            self.bookings.append(booking)
            self.booking_counter += 1

            print("\nBooking confirmed!")
            booking.display_summary()

        except ValueError:
            print("Error: Please enter valid numeric values.")

    def view_booking(self):
        if not self.bookings:
            print("\nNo booking found. Please book a flight first.")
        else:
            self.bookings[-1].display_summary()

    def run(self):
        while True:
            print("===== KIRAN AIR BOOKING =====")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please try again.")


# Create object and run the application
system = FlightBookingSystem()
system.run()