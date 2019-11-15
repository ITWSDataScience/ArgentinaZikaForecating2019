#this is the script I used to aggregate the data.
#the directories are hardcoded to the data's github repo, so they'll need modification before reuse.

import os
import pandas
import numpy
import math
for dir in os.listdir('data/'):
	files = os.listdir('data/'+dir)
	print("aggregating directory data/"+dir)
	total = pandas.read_csv('data/'+dir+'/'+files[0]).to_numpy()
	for i in range(1,len(files)):
		temp = pandas.read_csv('data/'+dir+'/'+files[i]).to_numpy()
		for idx in range(0,temp.shape[0]):
			found = False
			for idx2 in range(0,total.shape[0]):
				if temp[idx][1] == total[idx2][1] and temp[idx][3] == total[idx2][3]:
					found = True
					if math.isnan(total[idx2][7]):
						total[idx2][7] = temp[idx][7]
					elif not math.isnan(temp[idx][7]):
						total[idx2][7] = total[idx2][7]+temp[idx][7]
					continue
			if found==False:
				total = numpy.append(total,[temp[idx]],axis=0)
	print("writing aggregated data to file")
	f = open('data/'+dir+'.csv','w')
	f.write("report_date,location,location_type,data_field,data_field_code,time_period,time_period_type,value,unit\n")
	for i in range(0, total.shape[0]):
		for j in range(0, total.shape[1]-1):
			f.write(str(total[i][j])+",")
		f.write(total[i][total.shape[1]-1]+"\n")
	f.close()
	
