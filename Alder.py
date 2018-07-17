
def age():
    name = input("Whats ur name?")
    print(name)
    YearofBirth = input("What year where you born in?")
    print(YearofBirth)
    DateOfBirth = input("What date where you born on ?")
    print (DateOfBirth)
    CurrentYear = input("What year is it now?")
    print("it is the year", CurrentYear)
    YourAge = int(CurrentYear) - int(YearofBirth)
    print(YourAge)

    print("Your birth date is", YearofBirth, DateOfBirth, "This makes you", YourAge)

age()
