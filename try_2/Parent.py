from Person import Person, State
from Payment import Payment

class Parent(Person):
    def __init__(self, name, p_id, age, phone_number, status: State,payment:Payment, childrenList: list):
        """
        Initializes a Parent object with the provided attributes.
        :param name: The name of the parent.
        :param id: The ID of the parent.
        :param age: The age of the parent.
        :param phone_number: The phone number of the parent.
        :param status: The status of the parent (must be an instance of State).
        :param childrenList: A list of children (instances of Person).
        """
        super().__init__(name, p_id, age, phone_number, status)
        self.childrenList = childrenList  # Assign the list of children
        self.payment = payment # Assign the payment

    ################################################################################################################################

    # Getter and Setter for childrenList
    @property
    def childrenList(self):
        return self._childrenList

    @childrenList.setter
    def childrenList(self, value):
        """
        Validates that the childrenList is a list and each child is an instance of Person.
        """
        if isinstance(value, list) :
            self._childrenList = value
        else:
            raise ValueError("childrenList must be a list of Person instances.")

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, value):
        if not isinstance(value, Payment):
            raise ValueError("Payment must be an instance of Payment class.")
        self._payment = value

    ################################################################################################################################

    # __str__ method
    def __str__(self):
        base_str = super().__str__()  # Call to the __str__ of the Person class
        children_names = ', '.join([child.name for child in self.childrenList])  # Get the names of all children
        return f"{base_str}, Children: {children_names}"
