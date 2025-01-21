import datetime

# Task 1
date_1 = str(datetime.datetime.now().date())[-2::1]
# print(int(date_1) - 5)

# Task 2
yesterday = int(str(datetime.datetime.now().date())[-2::1]) - 1
today = int(str(datetime.datetime.now().date())[-2::1])
tomorrow = int(str(datetime.datetime.now().date())[-2::1]) + 1
# print(yesterday, today, tomorrow, sep=" - ")

# Task 3
date_3 = str(datetime.datetime.now())
ms = str(datetime.datetime.now().microsecond)
# print(date_3[0:len(date_3) - (len(ms)) - 1])

# Task 4
from datetime import datetime

date_1 = "2025-01-21 12:00:00"
date_2 = "2025-01-20 12:00:00"
date_format = "%Y-%m-%d %H:%M:%S"

datetime_1 = datetime.strptime(date_1, date_format)
datetime_2 = datetime.strptime(date_2, date_format)
minus = abs((datetime_2 - datetime_1).total_seconds())
print(minus)
