from datetime import datetime, date, timedelta
import numpy as np
import calendar

# print(list(calendar.day_name)[calendar.weekday(2020, 5, 27)])

start = datetime.date(datetime.today())
end = date(2020, 5, 27)

delta = end - start

cnt = cnt_reg = 0

for i in range(delta.days + 1):
    day = start + timedelta(days=i)
    yyyy, mm, dd = map(int, str(day).split('-'))

    # I am currently just working part time from Monday until Thursday
    if list(calendar.day_name)[calendar.weekday(yyyy, mm, dd)] not in ['Friday', 'Saturday', 'Sunday'] \
            and str(day) != '2020-05-21':  # This is a holiday here in Germany
        # print(day, list(calendar.day_name)[calendar.weekday(yyyy, mm, dd)])
        cnt += 1
    cnt_reg += 1

print(f'I will work {cnt} more days at adviqo :).')
print(f'{cnt_reg} regular days left')
