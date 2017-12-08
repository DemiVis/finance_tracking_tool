import os
import datetime


class AnnualPot:
    """
    Annual pot class for keeping track of pots of money that are spent on an
    annual basis.
    """

    def __init__(self, name, year, amount, description="", log_file=""):
        self.name = name
        self.year = year
        self.description = description
        self.amount = amount
        self.log_file = ""
        self.log_fp = None
        self.expenses = []

        if log_file is not "":
            self.open_log(log_file)

    def cleanup(self):
        if self.log_fp is not None:
            self.log_fp.close()

    def open_log(self, path):
        if path[-3:] != "txt":
            print "ERROR: ",
            print "Attempted to open log file '", path, "'"
            print "Log files should have the .txt extension and this does not!"
        self.log_file = path
        if not os.path.isfile(path):
            try:
                self.log_fp = open(path, "a+")
            except:
                print "An ERROR has occured!!"
                print "Log file for annual pot ", self.name, " could not be opened."
        else:
            print ("DIAG: Starting new log for Annual pot '" + self.name + "'" 
                   " at " + path)
            self.log_fp = open(path, "w+")
            self.log_action("Finances Log File\n"
                            "Log file for new Annual pot described below.")
            self.log_action("> Year:       " + self.year)
            self.log_action("> Name:       " + self.name)
            self.log_action("> Description:" + self.description)
            self.log_action("> Init Amount:" + self.amount)
            self.log_action("\n")

    def log_action(self, log_str, new_line=True):
        if self.log_fp is not None:
            try:
                self.log_fp.write("["+str(datetime.datetime.now())[:-7]+"] ")
                self.log_fp.write(log_str)
                if new_line:
                    self.log_fp.write("\n")
                return True
            except:
                return False
        else:
            return False

    def add_expense(self, expense):
        """ Add expense to annual pot, subtracting the expense amount from the
        annual pot amount.

        Returns the amount left in the annual pot
        """
        self.expenses.append(expense)
        self.log_action("Adding expense:")
        self.log_action("  Description: " + expense.description)
        self.log_action("  Amount:      " + str(expense.amount))

        self.amount = self.amount - expense.amount
        self.log_action("  New Balance: " + self.amount)

        self.log_action("", new_line=True)

        return self.amount

    def add_adjustment(self, amount, description):
        """ Add adjustment to annual pot, adding the adjustment amount to the
        annual pot amount.

        Returns the new amount left in the annual pot
        """
        self.log_action("Adding adjustment:  #################################")
        self.log_action("  Description: " + description)
        self.log_action("  Amount:      " + str(amount))

        self.amount = self.amount + amount
        self.log_action("  New Balance: " + self.amount)

        self.log_action("#####################################################",
                        new_line=True)

        return self.amount
