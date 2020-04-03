##########################
#  Exponential Decay     #
#        Rate            #
# Finding The Half-Life  #
#                        #
#    By Fin and Stacey   #
##########################

import math

Initial_Value = input('What is the initial value?')
Decay_Rate = input('What is the decay rate in decimal form?')
Decay_Rate = 1-float(Decay_Rate)
Previous = 0
Original_Decay_Rate = Decay_Rate
Time_Measurement = input('What is the measurement of time(Days, Weeks, Months, Years, etc...)?')
print("")
print('Loading... ===|===>')
print("")
Time = 0
while Decay_Rate > 0.5:
    Previous = Decay_Rate
    Decay_Rate = Previous*Original_Decay_Rate
    Time = Time+1
if Decay_Rate is 0.5:
    print("The Half-Life is "+Time+".")
else:
    Time_2 = int(Time)-1
    Time_2 = str(Time_2)
    print("The Half-Life is between "+str(Time)+" and "+Time_2+ Time_Measurement+".")
