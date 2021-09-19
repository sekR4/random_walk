

inp0 = '9 6 2015'
inp1 = '6 6 2015'
# 45

# inp0 = '31 8 2004'
# inp1 = '20 1 2004'
# 3500

# inp0 = '31 12 2009'
# inp1 = '1 1 2010'
# 0


d0, m0, y0 = map(int,inp0.split()) # return date
d1, m1, y1 = map(int,inp1.split()) # due date

years_between = y0 - y1
months_between = m0 - m1
days_between = d0 - d1

print(years_between, months_between, days_between)

if years_between > 0: fee_year = 10000
else: fee_year = 0

if months_between > 0 and years_between == 0: fee_month = 500
else: fee_month = 0

if days_between > 0 and months_between <= 0 and years_between <= 0: fee_day = 15
else: fee_day = 0

print(fee_year, fee_month, fee_day)

fee = fee_year + months_between * fee_month + days_between * fee_day
print(fee)
# 3500
