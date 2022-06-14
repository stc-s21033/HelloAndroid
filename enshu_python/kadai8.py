from datetime import date, timedelta as td
today = date.today()
one_week = td(days = 7)
td2 = today + one_week
print(td2.strftime('%B %d, %Y'))
