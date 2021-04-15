class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def mdy(cls, dmy_input):
        day, month, year = map(int, dmy_input.split("-"))
        print(day, month, year)
        return day, month, year

    @staticmethod
    def valid_date(dmy_input):
        day, month, year = map(int, dmy_input.split("-"))
        if day not in range(1,32) or month not in range (1,13):
            print("Введите корректные данные")
        pass

a = "31-12-2023"
Date.mdy(a)
Date.valid_date(a)

