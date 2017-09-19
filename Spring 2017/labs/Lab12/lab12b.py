class Time(object):
    """docstring for clock"""

    def __init__(self, hour=0, mins=0, secs=0):
        """ Construct a Time using three integers. """
        self.__hour = hour
        self.__mins = mins
        self.__secs = secs

    def __repr__(self):
        """ Return a string as the formal representation a Time. """
        out_str = "Class Time: {:02d}:{:02d}:{:02d}" .format(
            self.__hour, self.__mins, self.__secs)

        return out_str

    def __str__(self):
        """ Return a string as hr:min:sec representation a Time. """
        out_str = "{:02d}:{:02d}:{:02d}" .format(
            self.__hour, self.__mins, self.__secs)

        return out_str

    def from_str(self, time_str):
        """ Convert a string (yyyy-mm-dd) into a Date. """
        time_str = time_str.replace(' ', '')
        hour, mins, secs = [int(n) for n in time_str.split(':')]
        self.__hour = hour
        self.__mins = mins
        self.__secs = secs


#import clock
A=Time()
A.from_str('12:45:30')
print(A.__str__())
print(A.__repr__())