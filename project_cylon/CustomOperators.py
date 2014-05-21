# -*- coding: utf-8 -*-
import re

class Infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)

class NaturalOperator:
    """
    This class provide string compare operators in natural alphanumeric order.

    The original compare operators less than (<) and greather than (>) use computer alphanumeric
    while compare strings which is not the same behavior as human compare for example.

        print ( "5 USD" < "10 USD" ) >>> False

    So, this library defined new operators to solve this problem.

        print ( "5 USD" |less_than| "10 USD" ) >>> True
    """

    @classmethod
    def Sort(cls, unsortedList):
        """ Sort the list into natural alphanumeric order. """

        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]

        sortedList = list(unsortedList)
        sortedList.sort(key=alphanum_key)

        return sortedList

    @classmethod
    def LessThan(cls, value1, value2):
        """ Compare two strings with natural alphanumeric order. """

        unsortedList = []
        unsortedList.append(value1)
        unsortedList.append(value2)

        sortedList = cls.Sort(unsortedList)

        if unsortedList == sortedList and value1 != value2:
            return True
        else:
            return False

    @classmethod
    def MoreThan(cls, value1, value2):
        """ Compare two strings with natural alphanumeric order. """

        unsortedList = []
        unsortedList.append(value1)
        unsortedList.append(value2)

        sortedList = cls.Sort(unsortedList)
        sortedList.reverse()

        if unsortedList == sortedList and value1 != value2:
            return True
        else:
            return False

    @classmethod
    def Equal(cls, value1, value2):
        if value1 == value2:
            return True
        else:
            return False

    @classmethod
    def MoreThanOrEqual(cls, value1, value2):
        if cls.Equal(value1, value2) or cls.MoreThan(value1, value2):
            return True
        else:
            return False

    @classmethod
    def LessThanOrEqual(cls, value1, value2):
        if cls.Equal(value1, value2) or cls.LessThan(value1, value2):
            return True
        else:
            return False


##
## !!! declare natural sort operator !!!
##
natural_sort = NaturalOperator.Sort

##
## !!! declare compare operators !!!
##
equal = Infix(NaturalOperator.Equal)
more_than = Infix(NaturalOperator.MoreThan)
less_than = Infix(NaturalOperator.LessThan)
more_than_or_equal = Infix(NaturalOperator.MoreThanOrEqual)
less_than_or_equal = Infix(NaturalOperator.LessThanOrEqual)
