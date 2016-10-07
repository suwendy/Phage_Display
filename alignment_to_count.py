"""
This script coverts an alignment file into a counts matrix file,
i.e. print the randomer as often as its count dictates
"""

counts = open("/Users/erikburlingame/bioinformatics_project/rep1/protR3ctl_minus_compR3ctl_counts.txt", "rU")
alignment = open("/Users/erikburlingame/bioinformatics_project/rep1/protR3ctl_minus_compR3ctl_alignment.txt", "w")

for record in counts:
    record = record.strip().split("\t")
    for i in range(int(record[1])):
        alignment.write("{}\n".format(record[0]))

counts.close()
alignment.close()