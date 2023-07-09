def weekday_name(day_of_week):
    week_day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    if day_of_week >=1 and day_of_week <=7:
        return week_day[day_of_week-1]
    else:
        print ('none')

print(weekday_name(7))
print(weekday_name(1))
print(weekday_name(-1))
print(weekday_name(2))
print(weekday_name(5))
print(weekday_name(3))
print(weekday_name(100))
print(weekday_name(4))
print(weekday_name(12))


weekday_name(9)
weekday_name(10)
