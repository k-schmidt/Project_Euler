def div_100(year):
    return year % 100 == 0

def div_400(year):
    return year % 400 == 0

def div_4(year):
    return year % 4 == 0

class Year:

    days_of_week = {1, 2, 3, 4, 5, 6, 7}
    
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

def iter_year(start_year, end_year):
    start_day = get_start_day_of_year_given_previous(start_year - 1)
    for year in range(start_year, end_year + 1):
        yr = Year(year)
        i = 0
        for month in yr.months_days:
            i += month
            print(i)


if __name__ == '__main__':
    print(get_start_day_of_year_given_previous(1900))
    iter_year(1901, 2000)
