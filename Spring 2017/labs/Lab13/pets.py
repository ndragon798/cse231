
##
# Class PetError -- complete
##


class PetError(ValueError):

    pass

##
# Class Pet -- not complete
##


class Pet(object):

    def __init__(self, species=None, name=""):

        if species.lower() == 'dog' or species.lower() == 'cat'\
                or species.lower() == 'horse' or species.lower() == 'gerbil'\
                or species.lower() == 'hamster' or species.lower() == 'ferret':

            self.species_str = species.title()
            self.name_str = name.title()

        else:

            raise PetError()

    def __str__(self):
        if len(self.name_str) != 0:
            result_str = "Species of: {:s}, named {:s}".format(
                self.species_str, self.name_str)
        else:
            result_str = "Species of: {:s}, unamed".format(self.species_str)
        return result_str

##
# Class Dog -- not complete
##


class Dog(Pet):

    def __init__(self, name="", chase="Cats"):
        Pet.__init__(self, 'Dog', name)
        self.chase = chase.title()

    def __str__(self):
        if len(self.name_str) != 0:
            result_str = "Species of: {:s}, named {:s}, chases {:s}".format(
                self.species_str, self.name_str,self.chase)
        else:
            result_str = "Species of: {:s}, unamed, chases {:s}".format(self.species_str,self.chase)
        return result_str


##
# Class Cat -- not complete
##


class Cat(Pet):

    def __init__(self, name="", hates="Dogs"):
        Pet.__init__(self, 'Cat', name)
        self.hates = hates.title()

    def __str__(self):
        if len(self.name_str) != 0:
            result_str = "Species of: {:s}, named {:s}, hates {:s}".format(
                self.species_str, self.name_str,self.hates)
        else:
            result_str = "Species of: {:s}, unamed, hates {:s}".format(self.species_str,self.hates)
        return result_str
