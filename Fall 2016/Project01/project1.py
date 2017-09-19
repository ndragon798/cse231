print ("Wind Chill Conversion")
def calc_wct(atmp,aspd):
	return (35.74+(0.6215*atmp)-(35.75*(aspd**.16))+0.4275*atmp*(aspd**.16))

print("Temperature (degrees F): 15.0")
print("Wind speed (MPH): 10.0")
print("Wind Chill Temperature Index:",calc_wct(15.0,10.0))

print("Temperature (degrees F): 0.0")
print("Wind speed (MPH): 20.0")
print("Wind Chill Temperature Index:",calc_wct(0.0,20.0))

print("Temperature (degrees F): -15.0")
print("Wind speed (MPH): 30.0")
print("Wind Chill Temperature Index:",calc_wct(-15.0,30.0))

temp = input("Please enter the temperature (degress F): ")
wnds = input("Please enter the wind speed(MPH): ")

print("Temperature (degrees F): ",temp)
print("Wind speed (MPH): ", wnds)
print("Wind Chill Temperature Index:",calc_wct(int(temp),int(wnds)))
