import time
import datetime
import calendar
dt = datetime.date.today()
print("\n DISPLAYING CURRENT DATE AND TIME.. \n")
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", dt.strftime("%Y"))
print("Month of year: ", dt.strftime("%B"))
print("Week number of the year: ", dt.strftime("%W"))
print("Weekday of the week: ", dt.strftime("%w"))
print("Day of year: ", dt.strftime("%j"))
print("Day of the month : ", dt.strftime("%d"))
print("Day of week: ", dt.strftime("%A"))
print("\nDISPLAYING CALANDER FOR THE CURRENT MONTH..")
month = int(dt.month)
year = int(dt.year)
print("\n")
calendar.setfirstweekday(calendar.SUNDAY)
cal = calendar.monthcalendar(year, month)
if len(str(month)) == 1:
    month = '0%s' % month
# Header
print('|+++++++%s-%s++++++|'%(month, year))
print("|Su Mo Tu We Th Fr Sa|")
print("|--------------------|")
# display calendar
border = '|'
for week in cal:
    line = border
    for day in week:
        if day == 0:
            line +='   '
        elif len (str(day)) == 1:
            line += ' %d ' % day
        else:
            line += '%d ' % day
    # remove space in last column
    line = line[0:len(line) - 1]
    line += border
    print(line)
print('|--------------------|\n')
