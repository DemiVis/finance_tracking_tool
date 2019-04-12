# Reads the downloaded transactions in and creates a "conditioned"
# copy that has the following format
# columns: amount (-expense/+income), name, category, date, [other details]

import os

# string to add to end of file-name after conditioning
suffix = "_conditioned"

def condition_discover(filename):
    out_fil = filename.split(".")[0]+suffix+"."+filename.split(".")[1]
    print "Conditioned", filename, "into", out_fil
    out = open(out_fil, "w")
    out.write("Amount,Name,Category,Date, Post Date,Dscvr Category\n")
    src = open(filename, "r")
    for line in src:
        if "Description" in line:
            continue
        details = line.strip().split(",")
        try:
            float(details[3])
        except ValueError:
            out.write("ERROR, Problem with this line:,"+line)
            print "ERROR in", filename
        else:
            out.write(str(-1*float(details[3])) + ",")
            out.write(details[2] + ",")
            out.write(" ,")
            out.write(details[0] + ",")
            out.write(details[1] + ",")
            out.write(details[4] + "\n")

def condition_bofa(filename):
    out_fil = filename.split(".")[0]+suffix+"."+filename.split(".")[1]
    print "Conditioned", filename, "into", out_fil
    out = open(out_fil, "w")
    out.write("Amount,Name,Category,Date, Reference, Address\n")
    src = open(filename, "r")
    for line in src:
        if "Payee" in line:
            continue
        details = line.strip().split(",")
        try:
            float(details[4])
        except ValueError:
            out.write("ERROR, Problem with this line:,"+line)
            print "ERROR in", filename
        else:
            out.write(details[4] + ",")
            out.write(details[2] + ",")
            out.write(" ,")
            out.write(details[0] + ",")
            out.write(details[1] + ",")
            out.write(details[3] + "\n")

def condition_midfirst(filename):
    out_fil = filename.split(".")[0]+suffix+"."+filename.split(".")[1]
    print "Conditioned", filename, "into", out_fil
    out = open(out_fil, "w")
    out.write("Amount,Name,Category,Date,CheckNum,Description\n")
    src = open(filename, "r")
    for line in src:
        if "Description" in line or len(line) < 5:
            continue
        details_og = line.strip().split(",")
        details = details_og[0:3]
        details.append(details_og[3]+details_og[4]) # [3]
        details.append(details_og[5].replace("MERCHANT PURCHASE TERMINA",""))   # [4]
        details.append(" ")
        try:
            float(details[3])
        except ValueError:
            out.write("ERROR, Problem with this line:,"+line)
            print "ERROR in", filename
        else:
            out.write(details[3] + ",")
            if len(details[4]) > 1:
                out.write(details[4] + ",")
            else:
                out.write(details[2] + ",")
            out.write(" ,")
            out.write(details[0] + ",")
            out.write(details[1] + ",")
            out.write(details[2] + ",")
            if len(details) > 4:
                for itm in details[5:]:
                    out.write(itm+",")
            out.write("\n")

trans_dir = os.path.dirname(os.path.abspath(__file__))
print "checking for transaction files in", trans_dir
for trans_fil in os.listdir(trans_dir):
    if ".csv" in trans_fil:
        if suffix in trans_fil:
            continue
        elif "3337" in trans_fil:
            condition_bofa(trans_fil)
        elif "Discover" in trans_fil:
            condition_discover(trans_fil)
        else:
            condition_midfirst(trans_fil)
    else:
        print "skipping condition of non CSV", trans_fil

here = input("\nConditioning Complete")


