import jdcal # https://pyhdust.readthedocs.io/jdcal.html
import datetime

def age_date(date_age):
    parts = date_age.split(' ')
    julian_date = tuple(map(int,parts[0].split('/')[::-1]))
    age_days = 28*12*int(parts[1]) + 28*int(parts[2]) + int(parts[3])
    date = datetime.date(*jdcal.jd2gcal(*jdcal.jcal2jd(*julian_date))[:-1])
    days = datetime.timedelta(days=age_days)
    date = date + days
    year = date.year
    month = date.month
    day = date.day
    date = jdcal.jd2jcal(*jdcal.gcal2jd(year, month, day))
    year = pad_string(date[0],4)
    month = pad_string(date[1],2)
    day = pad_string(date[2],2)
    return day + "/" + month + "/" + year


def pad_string(integer, str_length):
    string = str(integer)
    padded = "0"*(str_length-len(string))+string
    return padded

test_cases = ["28/02/1500 0 0 2", "01/12/0061 0 1 3", "06/05/0432 1 1 1"]
for case in test_cases:
    print(age_date(case))