# The purpose of this script is to sort Abolute Q csv output files, parse them for microchambers that passed given fluoresence values thresholds,
# and assign lineage predictions based on the resulting values. Output files were generated from samples using 3 (FAM, VIC, ABY/NED) and 2
# (FAM, VIC) probes on ORF1a and Spike genes of SARS-CoV-2, respectively. 
# 
#

from datetime import date, datetime
import pandas as pd
import os

directory_path = () # add directory path.
directory_files = os.listdir(directory_path)
directory_files_list = [i for i in directory_files if i.endswith(('.csv'))]
directory_files_list.sort(key = str.split)

files_3395 = []
files_143 = []

for file in directory_files_list:
	i = file.split('_')
	if i[1] == '3395':
		files_3395.append(file)
	else:
		files_143.append(file)

df0 = pd.DataFrame()
df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()

# Thresholds, adjust as needed. 
microchambers_count = 20480 # Adjust for total number of microchambers. Ensures all microchamber data are accounted for. 
fam_fluo_threshold = 15000
vic_fluo_threshold = 2000
aby_fluo_threshold = 2300
total_pos_microchambers_threshold = 5 # Adjust to determine limit of detection. 

#reads file in directory and performs operations to determine total microchambers that have passed their probe specific fluoresence thresholds.
for file in files_3395:
	df = pd.read_csv(file)
	i = file.split('_')	
	print(i)
	unique_id = pd.Series(i[0][2:4] + '_' + i[3])
	total_datapoints_check = len(df.index) # Checks for total number of microchamers.
	if total_datapoints_check == microchambers_count:
		df = df[df.Reject != True] # Removes any rejected microchambers.
		if df.columns[7] == 'FAM_Target 1':
			df = df.rename(columns = {'FAM_Target 1': 'FAM_Target_1'})
			df = df[df.FAM_Target_1 >= fam_fluo_threshold] # Respective probe threshold check.
			passed_threshold = pd.Series(len(df.index)) 
			fdf_id = pd.DataFrame(unique_id, columns = ['Unique_id'])
			fdf_count = pd.DataFrame(passed_threshold, columns = ['3395_FAM_pos_count'])
			fdf = pd.concat([fdf_id, fdf_count], axis = 1)
			df1 = pd.concat([df1, fdf], axis = 0)
		elif df.columns[7] == 'VIC_Target 2':
			df = df.rename(columns = {'VIC_Target 2': 'VIC_Target_2'})
			df = df[df.VIC_Target_2 >= vic_fluo_threshold]
			passed_threshold = pd.Series(len(df.index))
			vdf_id = pd.DataFrame(unique_id, columns = ['Unique_id'])
			vdf_count = pd.DataFrame(passed_threshold, columns = ['3395_VIC_pos_count'])
			vdf = pd.concat([vdf_id, vdf_count], axis = 1)
			df2 = pd.concat([df2, vdf], axis = 0)
		elif df.columns[7] == 'ABY_Target 3':
			df = df.rename(columns = {'ABY_Target 3': 'ABY_Target_3'})
			df = df[df.ABY_Target_3 >= aby_fluo_threshold]
			passed_threshold = pd.Series(len(df.index)) 
			adf_id = pd.DataFrame(unique_id, columns = ['Unique_id'])
			adf_count = pd.DataFrame(passed_threshold, columns = ['3395_NED_pos_count']) # ABY probe name changed to NED.
			adf = pd.concat([adf_id, adf_count], axis = 1)
			df3 = pd.concat([df3, adf], axis = 0)

df1 = df1.set_index(['Unique_id'])
df2 = df2.set_index(['Unique_id'])
df3 = df3.set_index(['Unique_id'])
df0 = df1.join(df2)
df0 = df0.join(df3)

for file in files_143:
	df = pd.read_csv(file)
	i = file.split('_')
	print(i)
	unique_id = pd.Series(i[0][2:4] + '_' + i[3])
	total_datapoints_check = len(df.index)
	if total_datapoints_check == microchambers_count:
		df = df[df.Reject != True]
		if df.columns[7] == 'FAM_Target 1':
			df = df.rename(columns = {'FAM_Target 1': 'FAM_Target_1'})
			df = df[df.FAM_Target_1 >= fam_fluo_threshold]
			passed_threshold = pd.Series(len(df.index)) 
			fdf_id = pd.DataFrame(unique_id, columns = ['Unique_id'])
			fdf_count = pd.DataFrame(passed_threshold, columns = ['143_FAM_pos_count'])
			fdf = pd.concat([fdf_id, fdf_count], axis = 1)
			df4 = pd.concat([df4, fdf], axis = 0)
		elif df.columns[7] == 'VIC_Target 2':
			df = df.rename(columns = {'VIC_Target 2': 'VIC_Target_2'})
			df = df[df.VIC_Target_2 >= vic_fluo_threshold]
			passed_threshold = pd.Series(len(df.index))
			vdf_id = pd.DataFrame(unique_id, columns = ['Unique_id'])
			vdf_count = pd.DataFrame(passed_threshold, columns = ['143_VIC_pos_count'])
			vdf = pd.concat([vdf_id, vdf_count], axis = 1)
			df5 = pd.concat([df5, vdf], axis = 0)

df4 = df4.set_index(['Unique_id'])
df5 = df5.set_index(['Unique_id'])
df6 = df4.join(df5)
df0 = df0.join(df6)

# Block below is used to predict the lineage. Values over/under total_pos_microchambers_threshold are considered ambiguous/undetermined. 
# Blank cells return "Lineage" in prediction column. 

A = df0['3395_FAM_pos_count'] >= total_pos_microchambers_threshold 
a = df0['3395_FAM_pos_count'] < total_pos_microchambers_threshold
B = df0['3395_VIC_pos_count'] >= total_pos_microchambers_threshold
b = df0['3395_VIC_pos_count'] < total_pos_microchambers_threshold
C = df0['3395_NED_pos_count'] >= total_pos_microchambers_threshold
c = df0['3395_NED_pos_count'] < total_pos_microchambers_threshold
D = df0['143_FAM_pos_count'] >= total_pos_microchambers_threshold
d = df0['143_FAM_pos_count'] < total_pos_microchambers_threshold
E = df0['143_VIC_pos_count'] >= total_pos_microchambers_threshold
e = df0['143_VIC_pos_count'] < total_pos_microchambers_threshold

df0['3395_lineage_prediction'] = 'Lineage'

df0['3395_lineage_prediction'].loc[(A) & (b) & (c)] = 'BA.1'
df0['3395_lineage_prediction'].loc[(a) & (B) & (c)] = 'Delta'
df0['3395_lineage_prediction'].loc[(a) & (b) & (C)] = 'BA.2'
df0['3395_lineage_prediction'].loc[(a) & (b) & (c)] = 'Undetermined'
df0['3395_lineage_prediction'].loc[(A) & (B) & (C) |(a) & (B) & (C) |(A) & (b) & (C) |(A) & (B) & (c)] = 'Ambiguous'

df0['143_lineage_prediction'] = 'Lineage'

df0['143_lineage_prediction'].loc[(D) & (e)] = 'BA.1'
df0['143_lineage_prediction'].loc[(d) & (E)] = 'Delta/BA.2'
df0['143_lineage_prediction'].loc[(D) & (E)] = 'Ambiguous'
df0['143_lineage_prediction'].loc[(d) & (e)] = 'Undetermined'

outdate = datetime.today().strftime('%Y_%m_%d')
outfile = str('Combined_output')
df0.to_csv(outfile + '_' + outdate + '.csv')









