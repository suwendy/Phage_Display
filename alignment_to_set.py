
"""
This script removes duplicate appearances of peptides from alignment files, writing the core 'set' to another file
"""
handle = open("/Users/erikburlingame/bioinformatics_project/rep1/total_alignment.txt", "rU")
sets = open("/Users/erikburlingame/bioinformatics_project/rep1/total_set.txt", "w")

total = []

print("Reading in randomer alignment file...")

# Append all sequences in alignment to a list
for record in handle:
    total.append(record)

print("Removing duplicate randomers from alignment...")

# Lists have set functionality. Huzzah! Sort the set alphabetically.
reduced = sorted(set(total))

print("Writing randomer set file...")

# Write set to file
for i in reduced:
    sets.write("{}".format(i))

print("Randomer set file written successfully...")

handle.close()
sets.close()