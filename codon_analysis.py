"""
This script will:
1) Read the aligned.fasta files in a directory.
2) Parse out nt sequence string at loci of sequence input range.
3) Match probe/primer with nts at their location by index.
4) Determine the number of match and missmatch at each nt by index.
"""
import os
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from collections import Counter

# set as directory containing .fasta files.
path = ''
os.chdir(path)

target_codon = 'F486'
codon_nt_start = 23014 # Current window observes mutations at F486.
codon_nt_end = 23023

input_seq = 'GCTGCGTTATAGCTTGG' # probe or primer sequence.
target_seq_start = 22853  # first position of binding site.
target_seq_end = 22870  # last position of binding site.

input_seq = Seq(input_seq)
input_seq_complement = input_seq.complement()

# input_seq for querying forward strand, input_seq_complement for rev strand. Adjusted for 3'-5'.
seq_orientation = input_seq

file_list = []
loci_seq_list = []
nt_position_missmatch_list = []
nt_missmatch_list = []
amplicon_drop_list = []
nt_kv = []
nt_list = []
codon_list = []

# search for files in directory
for file in os.listdir(path):
    if file.endswith('.fasta'):
        file_list.append(file)

# parses each .fasta file in list
for file in file_list:
    for seq_record in SeqIO.parse(file, 'fasta'):
        seq = seq_record.seq
        nt_list.append(seq[23014:23023])
        # slice of each sequence based on defined endpoints, append to list
        target_loci = seq[target_seq_start: target_seq_end]
        # All sequences with N at the loci of interest get removed. 
        if 'N' in target_loci:
            amplicon_drop_list.append(target_loci)
        else:
            loci_seq_list.append(target_loci)
        # compares each nt of input and target
        for i, j in zip(enumerate(target_loci), enumerate(seq_orientation)):
            if i != j:  # only interested in missmatch, append to list
                nt_position_missmatch_list.append(i[0])
                nt_missmatch_list.append(i[1])
                nt_kv.append(i)
    for i in nt_list:
        codon_list.append(i[3:6])
codon_list.sort()
nt_kv.sort()
nt_missmatch_list.sort()

nt_position_missmatch_list.sort()
c3 = Counter(nt_position_missmatch_list)
df = pd.DataFrame(columns={'nt_position', 'count'})
df['nt_position'] = c3.keys()
df['count'] = c3.values()
df = df.set_index('nt_position')
df.index = df.index + 1

c1 = Counter(nt_kv)
c2 = Counter(nt_missmatch_list)
c2k = [i for i in c2]
df1 = pd.DataFrame()
df1['nt_kv'] = c1.keys()
df1['count'] = c1.values()
df1['nt'] = c1.keys()
for i in df1['nt_kv']:
    df1['nt_position'] = [i[0] + 1 for i in df1['nt_kv']]
    df1['nt'] = [i[1] for i in df1['nt_kv']]
for i in c2k:
    df1[i] = 0
for i, j in enumerate(df1['nt']):
    pos = 4
    if j == df1.columns[pos]:
        df1.at[i, df1.columns[pos]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 1]:
        df1.at[i, df1.columns[pos + 1]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 2]:
        df1.at[i, df1.columns[pos + 2]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 3]:
        df1.at[i, df1.columns[pos + 3]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 4]:
        df1.at[i, df1.columns[pos + 4]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 5]:
        df1.at[i, df1.columns[pos + 5]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 6]:
        df1.at[i, df1.columns[pos + 6]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 7]:
        df1.at[i, df1.columns[pos + 7]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 8]:
        df1.at[i, df1.columns[pos + 8]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 9]:
        df1.at[i, df1.columns[pos + 9]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 10]:
        df1.at[i, df1.columns[pos + 10]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 11]:
        df1.at[i, df1.columns[pos + 11]] = df1.at[i, 'count']
    elif j == df1.columns[pos + 12]:
        df1.at[i, df1.columns[pos + 12]] = df1.at[i, 'count']
        
total = Counter(codon_list)
df2 = df1.groupby(['nt_position']).sum()
df3 = pd.DataFrame(total.items(), columns=['codon_nt','count'])
df3 = df3.set_index('codon_nt')

# outfile1 = 'troubleshooting.csv'
outfile2 = 'probe_primer_seq_output.csv'
outfile3 = f'{target_codon}_codon_mutation_output.csv'

# df.to_csv(outfile1)
df2.to_csv(outfile2)
df3.to_csv(outfile3)

# counts total number of samples that failed 100% match
count = 0
for i in loci_seq_list:
    if i != seq_orientation:
        count += 1
total_sequences = len(loci_seq_list)
p_missmatch = count / total_sequences
p_match = 1 - p_missmatch
a = format(p_missmatch, '.2%')
b = format(p_match, '.2%')
print('\n'f'Total sequences that failed 100% match: {count}')
print(f'Total sequences: {total_sequences}''\n')
print(f'% of seq match: {b}')
print(f'% of seq missmatch: {a}')



