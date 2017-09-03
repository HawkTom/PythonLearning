import os  
path = r'C:\Users\Tom\Documents\py'
folders=[path]
results=[]
specify_str = 'test'
for folder in folders:
	for s in os.listdir(folder): 
		if os.path.isdir(os.path.join(folder,s)):
			folders += [os.path.join(folder,s)]
for folder in folders:
	for s in os.listdir(folder):
		if os.path.isfile(os.path.join(folder,s)) and specify_str in s:
			results += [s]
for file in results:
	print(file)

