
class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.passenger_name = None
        self.is_booked = False

class RailwayReservation:
    def __init__(self, total_seats=100):
        self.seats = [Seat(i + 1) for i in range(total_seats)]

    def book_ticket(self):
        seat_number = int(input(f"Enter seat number to book (1-{len(self.seats)}): "))
        
        if seat_number < 1 or seat_number > len(self.seats):
            print("Invalid seat number!")
            return

        seat = self.seats[seat_number - 1]
        
        if seat.is_booked:
            print("Seat already booked!")
            return
        
        name = input("Enter passenger name: ")
        seat.passenger_name = name
        seat.is_booked = True
        print("Ticket booked successfully!")

    def view_booked_tickets(self):
        print("\nBooked Tickets:")
        print("Seat Number\tPassenger Name")
        
        booked_any = False
        for seat in self.seats:
            if seat.is_booked:
                print(f"{seat.seat_number}\t\t{seat.passenger_name}")
                booked_any = True
        
        if not booked_any:
            print("No tickets booked yet.")

    def cancel_ticket(self):
        seat_number = int(input(f"Enter seat number to cancel (1-{len(self.seats)}): "))

        if seat_number < 1 or seat_number > len(self.seats):
            print("Invalid seat number!")
            return

        seat = self.seats[seat_number - 1]

        if not seat.is_booked:
            print("Seat not booked!")
            return

        seat.is_booked = False
        seat.passenger_name = None
        print("Ticket canceled successfully!")

def main():
    system = RailwayReservation()
    
    while True:
        print("\nRailway Reservation System")
        print("1. Book Ticket")
        print("2. View Booked Tickets")
        print("3. Cancel Ticket")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            system.book_ticket()
        elif choice == "2":
            system.view_booked_tickets()
        elif choice == "3":
            system.cancel_ticket()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
