"""
Financial tool for keeping track of finances
"""

from classes import Application
import cPickle as pickle
from Tkinter import *

################################################################################
# data_file_names
################################################################################
category_file = "data_files/categories.pkl"

################################################################################
# Helper functions
################################################################################


################################################################################
# Main
################################################################################
def main():
    root = Tk()
    application = Application.Application(root)
    application.mainloop()
    # let it run
    root.destroy()

if __name__ == "__main__":
    main()