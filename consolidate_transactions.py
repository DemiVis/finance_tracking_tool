import os

out_file = "Consolidated_Transactions.csv"

transactions = []

trans_dir = os.path.dirname(os.path.abspath(__file__))
print "checking for transaction files in", trans_dir
for trans_fil in os.listdir(trans_dir):
    if "categorized" in trans_fil:
        print "Reading",trans_fil,"..."
        if "3337" in trans_fil:
            acct = "BofA Credit"
        elif "Discover" in trans_fil:
            acct = "Discover"
        else:
            acct = "Midfirst"
            
        fil = open(trans_fil)
        for line in fil:
            if "Amount" in line and "Name" in line:
                continue
            parts = line.split(",")
            transactions.append([parts[3], parts[1], parts[0], parts[2], acct])

print "Sorting..."
transactions.sort(key=lambda x: x[0])

print "Writing transactions to", out_file
out = open(out_file, "a+")
for transaction in transactions:
    if "Skip" in transaction:
        continue
    if "investigate" in transaction:
        print "Found transaction the needs to be investigated!"
        print "    ",transaction
    out.write(",".join(transaction))
    out.write("\n")

here = input("\nConsolidation Complete")
