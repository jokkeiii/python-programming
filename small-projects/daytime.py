# ask for user to input time in hours 
# output time of day from a function

# function to test time of the day
def timeOfDay(clock):
    if clock >= 6 and clock <= 11:
        return "morning"
    elif clock >= 12 and clock <= 16:
        return "day"
    elif clock >= 17 and clock <= 22:
        return "evening"
    else:
        return "night"
