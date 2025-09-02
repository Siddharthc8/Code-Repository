import datetime
import pytz

# d = datetime.date(2016, 9, 20)
# print(d)
#
# print(datetime.date.today())                           # To print today's date
#
# today = datetime.date.today()                          # To print today's date
# print(today)
#
# print(today.year)                                      # To print just the year
# print(today.month)                                     # To print just the month
# print(today.day)                                       # To print just the day
#
# print(today.weekday())                                 # Monday 0 Sunday 6
# print(today.isoweekday())                              # Monday 1 Sunday 7
#
# # TIME DELTA               # Time delta is the difference between two dates and times
#
# tdelta = datetime.timedelta(days = 7)        # Time difference is set to 7 days
# print(today + tdelta)                        # Prints today's date plus the offset 7 days
# print(today - tdelta)                        # Prints today's date minus the offset 7 days
#
# # Date +/- Date is equal to Time delta
#
# bday = datetime.date(2024, 9, 20)
#
# till_bday = bday - today
# print(till_bday)
# # Output = 158 days, 0:00:00
#
# print(till_bday.days)                       # To print only the days
# print(till_bday.total_seconds())            # To print only the seconds
#
# tdy = datetime.time(9,30,45,100)
# print(tdy)
#
# tdy = datetime.datetime(2016, 9, 20, 10, 30, 45, 100000)
# print(tdy)
# print(tdy.year)
# print(tdy.month)
# print(tdy.day)
# print(tdy.hour)
# print(tdy.minute)
# print(tdy.second)
# print(tdy.microsecond)
#
# tdelta = datetime.timedelta(days = 7)
# print(tdy + tdelta)

# tdy_today = datetime.datetime.today()
# tdy_now = datetime.datetime.now()
# tdy_ctime = datetime.datetime.utcnow()
# print(tdy_today)
# print(tdy_now)
# print(tdy_ctime)

# dt = datetime.datetime(2024, 4, 27, 12, 30, 45, tzinfo=pytz.UTC)      # Time zone aware
# print(dt)
#
# dt_utcnow = datetime.datetime.now(tz = pytz.UTC)                        # Time zone aware
# print(dt_utcnow)

# dt_ct = datetime.datetime.now()
# ct_tz = pytz.timezone("US/Central")
#
# dt_ct = ct_tz.localize(dt_ct)
# print(dt_ct)

# Extra stuff

dt_ct = datetime.datetime.now(tz=pytz.timezone("US/Central"))
print(dt_ct.isoformat())                                      # Iso-format standard (International)
print(dt_ct.strftime("%B %d, %Y"))                            # Print it in the order you want

dt_str = "April 15, 2024"                                     # Just a string
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)