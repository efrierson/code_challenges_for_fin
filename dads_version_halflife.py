print("\n\n-----\n")
start_value = float(input("What is the starting value? "))
rate_of_decay = input("What is the rate of decay (as a percentage) ")
units = input("What unit is used to measure the time period (e.g., 'weeks')? ")
rate_of_decay = rate_of_decay.replace("%","")

try:
    float(rate_of_decay)
except ValueError:
    print("\n\n-----\n")
    print("That doesn't look like a percentage.  Try running this program again.")
    print("\n\n-----\n")
    quit()

rate_of_decay = float(rate_of_decay)
rate_of_decay = rate_of_decay / 100
rate_of_decay = 1 - rate_of_decay
if (rate_of_decay >= 1):
    print("\n\n-----\n")
    print("This is a growth equation, so there is no halflife.")
    print("\n\n-----\n")
    quit()

cumulative_percentage = rate_of_decay
count = 1
while (cumulative_percentage > .5):
    count = count + 1
    previous_percentage = cumulative_percentage
    cumulative_percentage = cumulative_percentage * rate_of_decay

print("\n\n-----\n")
print("The halflife is somewhere between "+str(count-1)+" and "+str(count)+" "+units+".")
print("The remaining amount of the original will be between "+str(start_value * cumulative_percentage)+" and "+str(start_value * previous_percentage)+".")
print("\n-----\n\n")