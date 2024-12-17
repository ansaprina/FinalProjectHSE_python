class Booking:
    def __init__(self, guest, table, date, start_time, end_time, num_guests):
        self.guest = guest
        self.table = table
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.num_guests = num_guests

    def get_details(self):
        return {
            'guest name': self.guest.name,
            'phone number': self.guest.phone_number,
            'table name': self.table.name,
            'date': self.date.strftime("%Y-%m-%d"),
            'start time': self.start_time.strftime("%H:%M"),
            'end time': self.end_time.strftime("%H:%M"),
            'number of guests': self.num_guests
        }
