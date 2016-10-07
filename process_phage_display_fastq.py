"""
This script reads in a fastq file from a phage display experiment and writes count and alignment files corresponding
to the 12-aa randomers encoded by the reads contained in that fastq.
"""

# Biopython: savior of souls
from Bio import SeqIO
from Bio import motifs
import operator # operator is useful for sorting dictionaries

handle = open("/Users/erikburlingame/bioinformatics_project/rep1/Naive_Library.fastq", "rU")
counts = open("/Users/erikburlingame/bioinformatics_project/rep1/naive_library12_counts.txt", "w")
alignment = open("/Users/erikburlingame/bioinformatics_project/rep1/naive_library12_alignment.txt", "w")

print("Initializing...")

# A dictionary is used as the data structure to count occurences of each randomer
d = {}

# Nifty counter to assure you that the script isn't bugging out while processing
counter = 1

for record in SeqIO.parse(handle, "fastq"):

    if counter % 100000 == 0:
        print("Processing read # {}...".format(counter))
    counter += 1

    if "GGGSAE" in record.seq.translate():  # Translates each read sequence
        rando = str(record.seq.translate().split("GGGSAE", 1)[0])   # Extract seq upstream of 'GGGSAE' flanking id sequence
        if len(rando) != 12:    # Return to to top of loop if randomer is not 12 aa in length
            continue
        if rando not in d: # Count randomer frequencies
            d[rando] = 1
        else:
            d[rando] += 1
        alignment.write("{}\n".format(rando))

print("FASTQ file processed successfully...")

print("Alignment file written successfully...")

print("Synthesizing counts matrix...")

# Alphabetically sort items in randomer frequency dictionary, write to counts matrix
for key, value in sorted(d.items(), key=operator.itemgetter(0)):
    counts.write("{}\t{}\n".format(key, value))

print("Count matrix written successfully...")

print("This concludes our program...GOOD DAY.")

handle.close()
counts.close()
alignment.close()