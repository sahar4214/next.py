def gen_secs():
    for sec in range(60):
        yield sec

def gen_minutes():
    for minute in range(60):
        yield minute

def gen_hours():
    for hour in range(24):
        yield hour
def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield f"{hour:02d}:{minute:02d}:{sec:02d}"
def gen_years(start=2019):
    year = start
    while True:
        yield year
        year += 1
def gen_months():
    for month in range(1, 13):
        yield month
def gen_days(month, leap_year=True):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        if leap_year:
            return 29
        else:
            return 28
def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in range(1, gen_days(month, year % 4 == 0) + 1):
                for time in gen_time():
                    yield f"{day:02d}/{month:02d}/{year} {time}"
gen_date_iter = gen_date()

for _ in range(1000000):
    next(gen_date_iter)

print(next(gen_date_iter))
