from random import randint
from randimal.animals import animals
from randimal.adjectives import adjectives
from randimal.displayoption import DisplayOption

class Randimal(object):

    def __init__(self, numberOfAdjectives=1, displayOption=DisplayOption.LOWERCASE_HYPHENATED):
        """
        """
        self._numberOfAdjectives = numberOfAdjectives
        self._displayOption = displayOption

    def get(self):
        """
        Gets a randimal with the current configuration
        """
        result = []

        for i in range(0, self._numberOfAdjectives):
            result.append(adjectives[randint(0, adjectives.__len__() - 1)])

        result.append(animals[randint(0, animals.__len__() - 1)])

        delimiter = " " if not 1 & self._displayOption.value else "-"
        joined = delimiter.join(result)

        if self._displayOption.value & 2:
            joined = joined.lower()

        return joined