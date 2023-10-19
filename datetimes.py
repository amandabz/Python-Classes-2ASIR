import datetime

first_current_time = datetime.datetime.now()
input("Espera unos segundos y pulsa ENTER")

second_current_time = datetime.datetime.now()

# more: https://www.w3schools.com/python/python_datetime.asp
print(first_current_time.year)
print(first_current_time.month)
print(first_current_time.strftime("%a"))  # weekday, short version
print(first_current_time.strftime("%A"))  # weekday, full version

print(first_current_time.strftime("%S"))  # seconds
print(second_current_time.strftime("%S"))  # seconds

