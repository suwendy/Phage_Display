#!/usr/bin/env python2.7


'''
This code will construct a matrix for all the counts for all the randomers under each condition
   
'''

import operator

abs_path = "/Users/WendySu/Desktop/Oregon/Fall_2016/Genomic_Methods/Phage_Dis_Project/data/Phage_Display_rep1"
total_set = open(abs_path+"/set_files/total_set.txt", "rU")

#this gives me a list of all randomers in the total set in a dictionary with the default value of ''

all_uniq_randomers = total_set.readlines()

total_set.close()

all_uniq_randomers_dict = {}

for randomer in all_uniq_randomers:
	randomer = randomer.strip('\n')
	all_uniq_randomers_dict[randomer] = ''

counts_dict = {}

#Column 1: "Naive", element 1
naive = open(abs_path+"/count_files/Naive_Library.counts.txt", "rU")
for read in naive:
	read = read.strip().split("\t")
	if read[0] in all_uniq_randomers_dict:
		if read[0] not in counts_dict: # create a list for the value of 19 elements
			counts_dict[read[0]] = [0]*19
		counts_dict[read[0]][0] = read[1] #assign the count number to the 1st element of the value of the read
	else: #if read[0] not in all_uniq_randomers_dict
		if read[0] not in counts_dict: # create a list for the value 
			counts_dict[read[0]] = [0]*19
		counts_dict[read[0]][0] = 0

#print counts_dict
naive.close()

''' 
Repeat code for all columns. Alternatively, I can create a loop to read in all the files.

'''

#write counts to a tab separated file

all_counts = open(abs_path+"/count_files/total_count_matrix.tsv", "w")

header = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % ("Randomer","Naive","Neg_1","Neg_2","Neg3","Protein_1","Protein_2","Protein_3","Protein_Neg_1","Protein_Neg_2","Protein_Neg_3", \
"Competitor_1","Competitor_2","Competitor_3","Competitor_Neg_1","Competitor_Neg_2","Competitor_Neg_3","Protein_Competitor_1",\
"Protein_Competitor_2","Protein_Competitor_3")

all_counts.write(header)
all_counts.write("\n")

for x in counts_dict:
	text = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (x, counts_dict[x][0], counts_dict[x][1], counts_dict[x][2], counts_dict[x][3], counts_dict[x][4], counts_dict[x][5], counts_dict[x][6], counts_dict[x][7], counts_dict[x][8], counts_dict[x][9], counts_dict[x][10], counts_dict[x][11], counts_dict[x][12], counts_dict[x][13], counts_dict[x][14], counts_dict[x][15], counts_dict[x][16], counts_dict[x][17], counts_dict[x][18])
	all_counts.write(text)
	all_counts.write("\n")
	
all_counts.close()
