#+======================================================================================+
# |Authors          : Kolli Hrudhay,Narendrababu S,Akshat Gupta,Potturi Mourya Chandra
# |Package          : Hospital Emergency
# |Module           : graph.py
# |Language         : Python 3.7
# |Description      : This is the module (which is called by the Assignment_code.py  
#					  module) in which the graph is traversed, the shortest distance 
#                     and path is calculated using Dijkstra’s algorithm.
#                     
#                     
#+======================================================================================+

import sys


class Graph:
	def __init__(self,nodes):
		# Constructer for the Graph class

		self.nodes=nodes
		self.graph=[[0 for i in range(nodes)] for j in range(nodes)]

	def minDist(self,dist,spSet):
		# This method will find the node with the minimum distance from a node
		# that is not yet included in the shortest path graph
		# and return the former node to the calling method(spAlgo).

		mindist=sys.maxsize

		for i in range(self.nodes):
			if dist[i] < mindist and spSet[i]==False:
				mindist=dist[i]
				min_index=i

		return min_index

		
	def spAlgo(self,src):
		# This method will find/identify the shortest distance and the path from a node to the other
		# by implemeting Dijkstra's single source shortest path algorithm
		# for a graph that is represented using adjacency matrix representation.

		maxnum=sys.maxsize
		dist=[maxnum]*self.nodes
		dist[src]=0
		spSet=[False]*self.nodes
		parent=[-1]*self.nodes
		

		for _ in range(self.nodes):

			ind1=self.minDist(dist,spSet)


			spSet[ind1]=True

			for ind2 in range(self.nodes):
				if self.graph[ind1][ind2] > 0 and spSet[ind2] == False and dist[ind2] > dist[ind1] + self.graph[ind1][ind2]:
					dist[ind2]=dist[ind1] + self.graph[ind1][ind2]
					parent[ind2]=ind1

		dict={}
		for i in range(1,self.nodes):
			temp=[]
			temp=self.path(parent,i,temp)
			
			dict[i]=[dist[i],temp]

		return dict

	def path(self,parent,i,temp):
		# This method will create the min distance path for each node from the source node.

		if parent[i]==-1:
			temp.append(0)
			return
		self.path(parent,parent[i],temp)
		temp.append(i)
		return temp