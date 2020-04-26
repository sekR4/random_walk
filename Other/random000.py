def imp_date_libs():
    from datetime import datetime, date, timedelta
    import calendar

    # return datetime, date, timedelta


# imp_date_libs()

# print(datetime.today())  # not callable with only importing libraries

# print(imp_date_libs().datetime.today()) # does also not work

from datetime import datetime, date, timedelta
import calendar

print(datetime.today())

# ok... importing libraries via a functions seems not to be a good idea
