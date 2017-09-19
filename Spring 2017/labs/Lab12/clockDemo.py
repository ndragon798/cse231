import clock

A=clock.Time()
A.from_str('12:45:30')
print(A.__str__())
print(A.__repr__())