# take "conditioned" files and edit with categories
# show user the line items that don't have category assigned and present
# them with categories to choose, edit file with selected category and
# save file.

import os
import Tkinter
from functools import partial
categories_file = "categories.txt"
suffix = "_categorized.csv"
lin = ""

def categorize(trans_file, categories):
    def update_cat(category):
        if "investigate" in category:
            print "Investigation needed in", trans_file
        # write the new line
        lin_list = lin.split(",")
        lin_list[2] = category
        out.write(",".join(lin_list))
        show_next_line()
        
    def show_next_line():
        # update to the next line item
        global lin
        lin = fil.readline()
        if lin.strip() == "":
            root.destroy()
        else:
            trans_dt.set(lin.split(",")[3])
            trans_desc.set(lin.split(",")[1])
            trans_amnt.set("${:,.2f}".format(float(lin.split(",")[0])))
            
    print "Categorizing", trans_file, "...",
    fil = open(trans_file, "r")
    out = open("_".join(trans_file.split("_")[:-1])+suffix, "a+")
    out.write(fil.readline()) # copy header row

    root = Tkinter.Tk()
    top = Tkinter.Frame(root)
    bot = Tkinter.Frame(root)
    left = Tkinter.Frame(top, width=400)
    right = Tkinter.Frame(top)

    trans_dt = Tkinter.StringVar()
    trans_desc = Tkinter.StringVar()
    trans_amnt = Tkinter.StringVar()
    Tkinter.Label(left, text="Transaction Date:", width=100).pack()
    Tkinter.Label(left, textvariable=trans_dt).pack()
    Tkinter.Label(left, text="Transaction Description:").pack()
    Tkinter.Label(left, textvariable=trans_desc).pack()
    Tkinter.Label(left, text="Transaction Amount:").pack()
    Tkinter.Label(left, textvariable=trans_amnt).pack()
    
    buttons = []
    for cat in categories:
        action = partial(update_cat, cat)
        buttons.append(Tkinter.Button(right, text=cat, fg="black",
                                      command = action, width=25
                                      ).pack())

    ext = Tkinter.Button(bot, text="QUIT",command=exit).pack()

    global lin
    lin = fil.readline()
    trans_dt.set(lin.split(",")[3])
    trans_desc.set(lin.split(",")[1])
    trans_amnt.set("${:,.2f}".format(float(lin.split(",")[0])))

    Tkinter.Label(root, text=trans_file).pack(side=Tkinter.TOP)
    top.pack(side = Tkinter.TOP)
    bot.pack(side = Tkinter.BOTTOM)
    left.pack(side = Tkinter.LEFT)
    #left.pack_propagate(False)
    right.pack(side = Tkinter.RIGHT)
    root.mainloop()
    print "DONE"


categories = []
for line in open(categories_file):
    categories.append(line.strip())
print "Categorizing into:"
print categories

trans_dir = os.path.dirname(os.path.abspath(__file__))
print "checking for transaction files in", trans_dir
for trans_fil in os.listdir(trans_dir):
    if "conditioned.csv" in trans_fil:
        categorize(trans_fil, categories)
    else:
        print "  Skipping categorization of", trans_fil

here = input("\nCategorization Complete")
