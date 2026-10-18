while True:
    print("\n--- CAB BOOKING CHATBOT ---")
    print("1. Book Ride")
    print("2. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        print("\n1. Auto - Rs.12/km")
        print("2. Sedan - Rs.18/km")
        print("3. SUV - Rs.25/km")

        cab = input("Choose cab: ")

        if cab == "1":
            rate = 12
            name = "Auto"
        elif cab == "2":
            rate = 18
            name = "Sedan"
        elif cab == "3":
            rate = 25
            name = "SUV"
        else:
            print("Invalid cab choice")
            continue

        print("\nSelect Route:")
        print("1. Pune Station to Shivajinagar - 5 km")
        print("2. Swargate to Kothrud - 8 km")
        print("3. Hinjawadi to Wakad - 10 km")
        print("4. Pune Station to Swargate - 6 km")
        print("5. Kothrud to Hinjawadi - 12 km")
        print("6. Wakad to Swargate - 15 km")
        print("7. Shivajinagar to Kothrud - 7 km")
        print("8. Pune Station to Hinjawadi - 18 km")
        print("9. Swargate to Wakad - 14 km")

        r = input("Choose route: ")

        if r == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif r == "2":
            source = "Swargate"
            destination = "Kothrud"
            distance = 8
        elif r == "3":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        elif r == "4":
            source = "Pune Station"
            destination = "Swargate"
            distance = 6
        elif r == "5":
            source = "Kothrud"
            destination = "Hinjawadi"
            distance = 12
        elif r == "6":
            source = "Wakad"
            destination = "Swargate"
            distance = 15
        elif r == "7":
            source = "Shivajinagar"
            destination = "Kothrud"
            distance = 7
        elif r == "8":
            source = "Pune Station"
            destination = "Hinjawadi"
            distance = 18
        elif r == "9":
            source = "Swargate"
            destination = "Wakad"
            distance = 14
        else:
            print("Invalid route choice")
            continue

        fare = rate * distance

        print("\n--- RIDE DETAILS ---")
        print("Cab:", name)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "per km")
        print("Total Fare: Rs.", fare)

        print("\n1. Confirm Ride")
        print("2. Cancel Ride")

        c = input("Enter choice: ")

        if c == "1":
            print("Your OTP is 1234")
            print("Booking Confirmed!")
            print("Ride cannot be cancelled after OTP sharing.")
        elif c == "2":
            print("Ride Cancelled!")
            print("OTP not shared.")
        else:
            print("Invalid choice. Ride not confirmed.")

    elif ch == "2":
        print("Thank you for using Cab Booking Chatbot!")
        break

    else:
        print("Invalid choice. Try again.")