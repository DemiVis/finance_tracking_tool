import Month
import AnnualPot
import datetime
import os


class Year:
    """
    Year class. All encapsulating class for all tool data. The only thing
    that gets exported and saved between sessions.
    """

    def __init__(self, name, sublogs_dir):
        self.name = name
        self._months = []
        self._annual_pots = []
        self._log_file = ""
        self._log_fp = None
        self._sublog_directory = sublogs_dir
        if not os.path.isdir(sublogs_dir):
            os.mkdir(sublogs_dir)

    def open_log(self, path):
        if path[-3:] != "txt":
            print "ERROR: ",
            print "Attempted to open log file '", path, "'"
            print "Log files should have the .txt extension and this does not!"
        self._log_file = path
        if not os.path.isfile(path):
            try:
                self._log_fp = open(path, "a+")
            except:
                print "An ERROR has occured!!"
                print "Log file for year ", self.name, " could not be opened."
        else:
            print ("DIAG: Starting new log for year '" + self.name + "'"
                   " at " + path)
            self._log_fp = open(path, "w+")
            self.log_action("Finances Log File\n"
                            "Log file for new Year", new_line=False)
            self.log_action(" (" + self.name + ") ")
            self.log_action("\n")

    def log_action(self, log_str, new_line=True):
        if self._log_fp is not None:
            try:
                self._log_fp.write("["+str(datetime.datetime.now())[:-7]+"] ")
                self._log_fp.write(log_str)
                if new_line:
                    self._log_fp.write("\n")
                return True
            except:
                return False
        else:
            return False

    def add_month(self, name):
        """ add new empty month to the year"""
        new_month = Month.Month(name, self.name)
        self._months.append(new_month)
        self.log_action("Adding new Month", new_line=False)
        self.log_action(" (" + name + ") ")
