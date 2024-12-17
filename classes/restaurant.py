from classes.table import Table
from classes.booking import Booking
from classes.guest import Guest
from datetime import datetime, timedelta


def take_table(table):
    table.mark_unavailable()
    return f"Table {table.name} is taken"


def release_table(table):
    table.mark_available()
    return f"Table {table.name} is released"


class Restaurant:
    def __init__(self):
        self.tables = []
        self.bookings = []

    def add_table(self, name, seats):
        for table in self.tables:
            if table.name == name:
                return None
        self.tables.append(Table(name, seats))
        return True

    def check_closest_booking(self, table, date, time_start):
        for booking in self.bookings:
            if booking.table == table and booking.date == date \
                    and (booking.start_time < time_start + timedelta(hours=3)
                         or booking.end_time > time_start - timedelta(hours=1)):
                return True
        return False

    def check_booking_availability(self, table, date, time_start, time_end):
        for booking in self.bookings:
            if booking.table == table and booking.date == date:
                if booking.start_time <= time_start <= booking.end_time or time_start <= booking.start_time <= time_end:
                    return False
                else:
                    if time_end + timedelta(hours=1) <= booking.start_time \
                            or booking.end_time + timedelta(hours=1) <= time_start:
                        return True
                    else:
                        return False
        return True

    def check_upcoming_bookings(self, table):
        for booking in self.bookings:
            if table == booking.table and datetime.now().date() == booking.date \
                    and datetime.now().time() < booking.end_time:
                return True
            elif table == booking.table and datetime.now().date() < booking.date:
                return True
        return False

    def get_available_tables(self, num_seats, is_booking, date, time_start=None, time_end=None):
        available_tables = []
        if not is_booking:
            for table in self.tables:
                if table.is_available and table.seats >= num_seats \
                        and not self.check_closest_booking(table, date, time_start):
                    available_tables.append(table)
        else:
            for table in self.tables:
                if table.seats >= num_seats:
                    if self.check_booking_availability(table, date, time_start, time_end):
                        available_tables.append(table)
                        return available_tables
        return available_tables

    def add_booking(self, guest, phone_number, date, start_time, end_time, num_guests):
        tables = self.get_available_tables(num_guests, True, date, start_time, end_time)
        if not tables:
            return None
        else:
            table = tables[0]
            booking = Booking(Guest(guest, phone_number), table, date, start_time, end_time, num_guests)
            self.bookings.append(booking)
            return booking

    def delete_booking(self, booking):
        if booking in self.bookings:
            self.bookings.remove(booking)
            return f"Booking for {booking.guest.name} at table {booking.table.name} has been deleted"
        return "Booking not found"

    def delete_table(self, table_name):
        for table in self.tables:
            if table.name == table_name and table.is_available and not self.check_upcoming_bookings(table):
                self.tables.remove(table)
                return None
            elif table.name == table_name and table.is_available and self.check_upcoming_bookings(table):
                return f"Table {table_name} is currently booked and cannot be deleted"
            elif table.name == table_name and not table.is_available:
                return f"Table {table_name} is currently taken and cannot be deleted"
        return "Table not found"
