""" Name: Matthew Strange
    Class: CS2420
    Date: 02/06/2021

    Description: Contains class for Course objects
"""


class Course:
    """Creates class object containing course information"""

    def __init__(self, _number=0, _name="", _credit=0.0, _grade=0.0, next=None):
        if not isinstance(_number, int) or _number < 0 or not isinstance(_name, str) or \
                not isinstance(_credit, float) or _credit < 0 or \
                not isinstance(_grade, float) or _grade < 0:
            raise ValueError
        self._number = _number
        self._name = _name
        self._credit = _credit
        self._grade = _grade
        self.next = next

    def number(self):
        """retrieves course number as an integer"""
        return int(self._number)

    def name(self):
        """retrieves course name as a string"""
        return str(self._name)

    def credit_hr(self):
        """retrieves credit hours as float"""
        return float(self._credit)

    def grade(self):
        """retrieves grade as float"""
        return float(self._grade)

    def __str__(self):
        """returns a string representing a single course"""
        return "cs{} {} Grade:{} Credit Hours: {}\n".\
            format(self._number, self._name, self._grade, self._credit)
