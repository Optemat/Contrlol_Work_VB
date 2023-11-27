class Invoice:
    def __init__(self):
        self.positions = []

    def add_position(self, position):
        self.positions.append(position)
