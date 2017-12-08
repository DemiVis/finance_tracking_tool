import os
import datetime


class Month:
    """
    Class to hold totals for a month's worth of expenses.
    """

    def __init__(self, name, year, log_file=""):
        self.name = name
        self.year = year
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
                print "Log file for month ", self.name, " could not be opened."
        else:
            print ("DIAG: Starting new log for Annual pot '" + self.name + "'" 
                   " at " + path)
            self.log_fp = open(path, "w+")
            self.log_action("Finances Log File\n"
                            "Log file for new Month", new_line=False)
            self.log_action(" (" + self.name + self.year + ") ")
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
        pass