class Table:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats
        self.is_available = True

    def mark_available(self):
        self.is_available = True

    def mark_unavailable(self):
        self.is_available = False
