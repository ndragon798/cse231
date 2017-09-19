###########################################################
    #  Computer Project #1
    #	Prompt for number of rods
    #	Convert rods to different units
    #	Return converted measurements.
###########################################################
#The next 2 lines read in amount of rods and converts them to float
num_rods =input("Input rods: ") 
num_rods=float(num_rods)
#This returns the number of rods input
print("You input",num_rods,"rods.")
#The next 5 lines convert rods to the designated unit
num_meters=(5.0292 *num_rods)
num_feet=(num_meters/0.3048)
num_miles=(num_meters/1609.34)
num_furlongs=(num_rods/40)
num_min=num_miles/(3.1/60)
#The next five lines return the converted units.
print("Conversions")
print("Meters:", num_meters)
print("Feet:", num_feet)
print("Miles:", num_miles)
print("Furlongs", num_furlongs)
print("Minutes to walk",num_rods,"rods:", num_min)