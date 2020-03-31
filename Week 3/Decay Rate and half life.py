##########################
#  Exponential Decay     #
#        Rate            #
# Finding The Half-Life  #
#                        #
#    By Fin and Stacey   #
##########################

import math

Initial_Value = input('What is the initial value?')
Shrinking_Initial_Value = Initial_Value
Decay_Rate = input('What is the decay rate in decimal form?')
Time_Measurement = input('What is the measurement of time(Daily, Weekly, Monthly, Yearly, etc...)?')
print("")
print('Loading... ===|===>')
print("")
Time = 0
while int(Initial_Value) // int(Shrinking_Initial_Value) < '2' :
    Time = Time + 1
    Shrinking_Initial_Value = Initial_Value*(1-Decay_Rate)**Time
    print(Shrinking_Initial_Value)
