# ask for user to input time in hours 
# output time of day from a function

# function to test time of the day
def timeOfDay(clock):
    if clock >= 6 and clock <= 11:
        return "morning."
    elif clock >= 12 and clock <= 16:
        return "day."
    elif clock >= 17 and clock <= 22:
        return "evening."
    else:
        return "night."

# ask user input
clock = int(input("Enter current time in hours: "))

# call function with user input and assign it to variable
time = timeOfDay(clock)

# print user input and function return from a variable
print("Current time is",clock,"hours and the time of day is",time)