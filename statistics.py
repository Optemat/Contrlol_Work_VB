class Statistics:
    def __init__(self, total_count, positions_count, total_earning):
        self.total_count = total_count
        self.positions_count = positions_count
        self.total_earning = total_earning

    def __str__(self):
        return (f'Всего продано товаров: {self.total_count}\n'
                f'сколько товаров продано по наименованиям: {self.positions_count}\n'
                f'суммарная выручка: {self.total_earning}\n')
