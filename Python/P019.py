def div_100(year):
    return year % 100 == 0

def div_400(year):
    return year % 400 == 0

def div_4(year):
    return year % 4 == 0

class Year:

    def __init__(self, year):
        "Used to calculate data about the days in the year"
        self.year = year
        self._feb_days = None
        self._year_days = None
        self.months_days = [31, self.feb_days, 31, 30,
           31, 30, 31, 31, 30, 31, 30, 31] 
        
    @property
    def feb_days(self):
        if self._feb_days is None:
            if self._leap_yearp():
                self._feb_days = 29
            else:
                self._feb_days = 28
        return self._feb_days

    @property
    def year_days(self):
        if self._year_days is None:
            if self._leap_yearp():
                self._year_days = 366
            else:
                self._year_days = 365
        return self._year_days

    def _leap_yearp(self):
        if (div_100(self.year) and div_400(self.year)
        or div_4(self.year) and not div_100(self.year)):
            return True
        return False

def get_start_day_of_year_given_previous(year, start_day=2):
    yr = Year(year)
    print(yr.year_days)
    _, rem = divmod(yr.year_days, len(yr.days_of_week))
    return start_day + rem

def increase_weekday(day):
    if day == 7:
        return 1
    return day + 1

def iter_year(start_year, end_year):
    start_day = get_start_day_of_year_given_previous(start_year - 1)
    count = 0
    for year in range(start_year, end_year + 1):
        yr = Year(year)
        for month in yr.months_days:
            for day in range(1, month + 1):
                if day == 1 and start_day == 1:
                    count += 1
                start_day = increase_weekday(start_day)
                print(year, month, day, start_day, count)
    return count

if __name__ == '__main__':
    print(get_start_day_of_year_given_previous(1900))
    print(iter_year(1901, 2000))
