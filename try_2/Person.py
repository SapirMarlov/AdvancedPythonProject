
from enum import Enum
from abc import ABC, abstractmethod

class State(Enum):
    """
    Represents a state for the Person object.
    """
    st1 = 'st1'
    st2 = 'st2'
    st3 = 'st3'
    st4 = 'st4'
    st5 = 'st5'
    st6 = 'st6'



class Person(ABC):
    def __init__(self, name, id, age, phone_number, status: State):
        """
        Initializes a Person object with the provided attributes.
        :param name: The name of the person (string, at least 3 characters).
        :param id: The ID of the person (integer, greater than 0).
        :param age: The age of the person (integer, between 18 and 69).
        :param phone_number: The phone number of the person (string, in the format XXX-XXXXXXX).
        :param status: The status of the person (must be an instance of State).
        """
        self.name = name
        self.id = id
        self.age = age
        self.phone_number = phone_number
        self.status = status
#getters and setters
################################################################################################################################
    # Name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        """
        Validates and sets the name.
        """
        if isinstance(value, str) and len(value) > 1:
            self._name = value
        else:
            raise ValueError("Name must be a string with more than 2 characters.")


    # ID property
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        """
        Validates and sets the ID.
        """
        if isinstance(value, int) and value > 0:
            self._id = value
        else:
            raise ValueError("ID must be a number greater than 0.")

    ################################################################################################################################

    # Age property
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        """
        Validates and sets the age.
        """
        if isinstance(value, int) and 18 <= value <= 69:
            self._age = value
        else:
            raise ValueError("Age must be a number between 18 and 69.")

    ################################################################################################################################

    # Phone number property
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        """
        Validates and sets the phone number.
        """
        pattern = r"^\d{2}-\d{7}$" #ביטוי רגולרי לבדיקה 052-9483722
        if isinstance(value, str)  :
            self._phone_number = value
        else:
            raise ValueError("Phone number must be str and len is 10 . ")

    ################################################################################################################################

    # Status property
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        """
        Validates and sets the status.
        """
        if isinstance(value, State):
            self._status = value
        else:
            raise ValueError("Status must be of type State.")

    ################################################################################################################################

    # __str__ method
    def __str__(self):
        return (f"Person(Name: {self.name}, ID: {self.id}, Age: {self.age}, "
                f"Phone: {self.phone_number}, Status: {self.status})")

    ################################################################################################################################

    # __eq__ method
    def __eq__(self, other):
        """
        Compares two Person objects based on their IDs.
        """
        if isinstance(other, Person):
            return self.id == other.id
        return False
