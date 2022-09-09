"""
Write a class Train which has a methods to book a ticket, get status(no of seats)
and get fare information of trsins running under Indian Railways
"""


class Train:
    def __init__(self):
        self.seats = 78
        self.price = 700

        pass

    def book_ticket(self):
        self.seats -= 1  # Each time a ticket is booked, number of seats decreases by 1

    def get_status(self):
        return self.seats

    def get_fare_info(self):
        return self.price


musa = Train()
musa.book_ticket()
print(musa.get_status())
musa.book_ticket()
print(musa.get_status())
print(musa.get_fare_info())
