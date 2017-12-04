"""
Expense class

"""

class Expense:
    """
    A class to encapsulate the information for a single expense.
    """

    def __init__(self, name="", amount=0.0, account="unknown"):
        self.name = name
        self.amount = amount
        self.account = account