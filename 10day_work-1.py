import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "Leap year"
      else:
        return "Not leap year"
    else:
      return "Leap year"
  else:
    return "Not leap year"



def days_in_month(year_test,month_test):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  value=month_test-1
  if month == 2 and is_leap(year_test):
        return f"Leap Year- Month: 2 days of Month : 29"       
  else:
    return f"Not Leap Year! Month: {month_test} days of Month: {month_days[value]}"
  
    

year = int(input("Enter a year: ")) 
month = int(input("Enter a month: ")) 
days = days_in_month(year, month)
print(days)

