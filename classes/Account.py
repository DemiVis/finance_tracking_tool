import datetime
import os

class Account:
    """ Class to keep track of the balance on an account.
    valid options for 'type' are 'credit' or 'debit' only
    if type==credit init_amount should be negative, else positive integer"""
    def __init__(self, name, init_amount, type, log_file=""):
        if type == "debit" or type == "credit":
            self.acc_type = type
        else:
            print "ERROR initializing account %s!" % name,
            print "  Account type '%s' is invalid" % type
            exit(-1)

        if type == "credit":
            if init_amount <= 0:
                self.balance = init_amount
            else:
                print "ERROR Initial amount for credit account %s " % name,
                print "is >= 0. Should be <0 since its a credit account!"
                exit(-1)
        elif type == "debit":
            if init_amount >= 0:
                self.balance = init_amount
            else:
                print "ERROR Initial amount for debit account %s " % name,
                print "is < 0. Should be >= 0 since its a debit account!"
                exit(-1)

        self.name = name
        self.log_fp = None
        self.log_file = log_file
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
                print "Log file for Account ",self.name, " could not be opened."
        else:
            print ("DIAG: Starting new log for Account '" + self.name + "'"
                   " at " + path)
            self.log_fp = open(path, "w+")
            self.log_action("Finances Log File\n"
                            "Log file for new Account", new_line=False)
            self.log_action(" (" + self.name + ") ")
            self.log_action("\n")

    def log_action(self, log_str, new_line=True):
        if self.log_fp is not None:
            try:
                self.log_fp.write(
                    "[" + str(datetime.datetime.now())[:-7] + "] ")
                self.log_fp.write(log_str)
                if new_line:
                    self.log_fp.write("\n")
                return True
            except:
                return False
        else:
            return False

    def get_balance(self):
        return self.balance

    def add_expense(self, expense):
        """ Add expense to account, subtracting the expense amount from the
        account balance.

        Returns the new balance
        """
        self.log_action("Adding expense:")
        self.log_action("  Description: " + expense.description)
        self.log_action("  Amount:      " + str(expense.amount))

        self.balance = self.balance - expense.amount
        self.log_action("  New Balance: " + self.balance)

        self.log_action("", new_line=True)

        return self.balance

    def add_debit(self, amount, description=""):
        """ Add debit to account, adding the amount to the account balance.

        Returns the new balance.
        """
        if self.acc_type == "debit":
            self.log_action("Adding debit:")
            self.log_action("  Description: " + description)
        elif self.acc_type == "credit":
            self.log_action("Adding payment:")

        self.log_action("  Amount:      " + str(amount))

        self.balance = self.balance + amount
        self.log_action("  New Balance: " + self.balance)

        self.log_action("", new_line=True)

        return self.balance
