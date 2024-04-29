def hello_func():
    print("Hello World")

hello_func()

def hello_func2():
    return "Hello World"

print(hello_func2())

def leap_year(year):
    if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
        print(year, " is a leap year")
    else:
        print(year, " is not a leap year")
leap_year(2004)