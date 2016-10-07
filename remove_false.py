"""
This script was designed to remove false positives from our experimental "protein only" data by subtracting
negative control alignments from their respective round of "protein only" alignments
"""

from itertools import chain
import operator

prot = open("/Users/erikburlingame/bioinformatics_project/rep1/protein_only_round3_minus_negR3_counts.txt", "rU")
neg = open("/Users/erikburlingame/bioinformatics_project/rep1/100uMcompetitor_round3_minus_negR3_counts.txt", "rU")
prot_minus_neg = open("/Users/erikburlingame/bioinformatics_project/rep1/protR3ctl_minus_compR3ctl_counts.txt", "w")

total = {}
for record in prot:
    record = record.strip().split("\t")
    total[record[0]] = record[1]

for i in neg:
    i = i.strip().split("\t")
    if i[0] in total:   # If a given randomer appears in the negative control...
        new_count = int(total[i[0]]) - int(i[1])    # Subtract its count from the corresponding prot only count
        if new_count <= 0:  # Negative counts don't make much sense (or do they?), so delete such entries.
            del total[i[0]]
        else:
            total[i[0]] = str(new_count)

# Alphabetically re-sort the prot_minus_neg counts
for key, value in sorted(total.items(), key=operator.itemgetter(0)):
    prot_minus_neg.write("{}\t{}\n".format(key, value))

prot.close()
neg.close()
prot_minus_neg.close()
