#import datetime

""" def next_birthday(fecha):
    date_format = "%d/%m/%Y"
    date = datetime.datetime.strptime(fecha, date_format)
    year = date.year
    if year % 4:
        while year % 4:
            year +=1 
        birthday = datetime.date(year, 2, 29)
    else:
        this_year_birthday = datetime.date(year, 2, 29)
        if date < this_year_birthday:
            birthday = this_year_birthday
        else:
            birthday = datetime.date(year+4, 2, 29)
    return datetime.datetime.strftime(birthday, date_format) """


def next_birthday(date):
    parts = list(map(int,date.split("/")))
    year = parts[2]
    if year % 4:
        year +=1 
        while year % 4:
            year +=1
    else:
        if parts[1] <= 2 and parts[0] < 29:
            pass
        else:
            year += 4
    day = "29"
    month = "02"
    year_string = str(year)
    year = "0"*(4-len(year_string)) + year_string
    return day + "/" + month + "/" +  year
    
        
        
    
test_cases = ["04/12/0061", "29/02/1500", "01/01/0444"]
for case in test_cases:
    print(next_birthday(case))