#+======================================================================================+
# |Authors          : Kolli Hrudhay,Narendrababu S,Akshat Gupta,Potturi Mourya Chandra
# |Package          : Hospital Emergency
# |Module           : Assignment_code.py
# |Language         : Python 3.7
# |Description      : This is the main module(script file) to be executed which 
#                     will read input from 'inputPS6.txt'file and call the 
#                     functions/methods from their respective modules, finally write 
#					  the output to the outputPS6.txt file.
#                     
#+======================================================================================+

from readingFun import readingFun as RF
from graph import Graph

# Formatted output of the input obtained from inputPS6.txt
elements1,elements2=RF('inputPS6.txt')

# A dictionary of nodes with the distance between them 
# is created for ease of mapping between the nodes.
if elements1:
	if elements2:
		nodesdict={}
		for i in elements1:
			nodesdict[i[0],i[1]]=i[2]

		# This part of code creates a list of nodes present/available.
		nodekeys=[]
		for i in nodesdict.keys():
			for j in i:
				nodekeys.append(j)

		nodekeys=list(set(nodekeys))
		nodekeys.sort()

		# Here, a Graph object is created.
		go=Graph(len(nodekeys))


		# This part of code is used to map an alphabet with a number.
		aplhadict={}
		aplhadict[elements2[0][1]]=0
		aplhadict[elements2[1][1]]=len(nodekeys)-1
		count=1
		for i in nodekeys:
			if i not in aplhadict:
				aplhadict[i]=count
				count+=1

		# This part of code is used to re-map a number with its respective alphabet.
		numdict={}
		for i in aplhadict:
			numdict[aplhadict[i]]=i


		# This part of code is used to create the adjacency matrix representation of the graph.
		for i in nodesdict:
			go.graph[aplhadict[i[0]]][aplhadict[i[1]]]=go.graph[aplhadict[i[1]]][aplhadict[i[0]]]=int(nodesdict[i[0],i[1]])

		# This part of code is used to create dictionary of paths for the nodes represented by numbers.
		numpaths=go.spAlgo(0)

		for i in numpaths.keys():
			for j in range(len(numpaths[i][1])):
				numpaths[i][1][j]=numdict[numpaths[i][1][j]]

		# This part of code is used to create dictionary of paths for the nodes represented by alphabets
		# as originally provided.
		alpaths={}
		for i in numpaths.keys():
			alpaths[numdict[i]]=numpaths[i]


		# This part of code is used to calculate the time it takes for the travel from hospital to airport.
		time=str((alpaths[elements2[1][1]][0]/80)*60)
		if '.' in str(time):
			temp1=time.split('.')
			temp1[1]=str(int(temp1[1])*60)[:2]
			if temp1[1]=='0':
				temp1[1]='00'
			time=':'.join(temp1)

		# This part of code will write the required output to the outputPS6.txt.
		with open('outputPS6.txt','w') as f1:
			f1.write("Shortest route from the hospital "+"'"+elements2[0][1]+"' "+"to reach the airport "+"'"+str(elements2[1][1])+"'"+" is "+str(alpaths[elements2[1][1]][1])+" and it has minimum travel distance "+str(alpaths[elements2[1][1]][0])+" km.")
			f1.write("\nIt will take "+time+" minutes for the ambulance to reach the airport.")

	else:
		with open('outputPS6.txt','w') as f2:
			f2.write("Hospital and Airport nodes are not provided.")

else:
	with open('outputPS6.txt','w') as f1:
		f1.write("There are no nodes and there distances provided to work on.")