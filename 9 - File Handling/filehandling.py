import numpy as np

filedata = np.genfromtxt('data.txt',delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

# Boolean Masking 
numbool = filedata > 20

# Get numbers > 20
num = filedata[filedata > 20]
print(num)