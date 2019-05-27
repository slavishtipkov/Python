class Fibbonator:
    fibbo_first = 1
    fibbo_second = 1

    fibbo_array = [fibbo_first, fibbo_second]

    def __init__(self, fibbo_number_count):
        self.fibbo_number_count = fibbo_number_count


    def run(self):
        if self.fibbo_number_count == 1:
            return [self.fibbo_first]

        if self.fibbo_number_count == 2:
            return self.fibbo_array

        index = 2

        for fib in self.fibbo_number_count:
