import statistics as stat


class InvoiceEditor:
    def __init__(self):
        self.invoices = []

    def add(self, invoice):
        self.invoices.append(invoice)

    def get_statistics(self):
        total_count = 0
        positions_count = {}
        total_earning = 0
        for invoice in self.invoices:
            total_count += len(invoice.positions)
            for position in invoice.positions:
                total_earning += position.price
                if position.name not in positions_count:
                    positions_count[position.name] = 1
                else:
                    positions_count[position.name] += 1

        return stat.Statistics(total_count, positions_count, total_earning)

    def delete(self):
        del self.invoices[-1]
