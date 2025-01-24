class Payment:
    def __init__(self, income, outcome):
        self.income = income
        self.outcome = outcome

    @property
    def income(self):
        return self._income

    @income.setter
    def income(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Income must be a number (int or float).")
        self._income = value

    @property
    def outcome(self):
        return self._outcome

    @outcome.setter
    def outcome(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Outcome must be a number (int or float).")
        self._outcome = value
########################################################################################################################################
    def create_pay_report(self):
        pass
    ########################################################################################################################################
    def __str__(self):
        return f"Payment(income={self.income}, outcome={self.outcome})"
