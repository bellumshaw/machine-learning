



with open ('rcd.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		print (row)
#open the csv and read the data by python

import numpy as np
data = np.loadtxt("rcd2.csv", delimiter=',', unpack = True)
print (data)
#open and read the file by numpy, the data change the
#style into tuple

