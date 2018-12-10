##################################
### author: Avinash Somanathan ###
##################################


from random import randrange
import dataStructure
import parserNetwork
import pdb
import AlgFuns
import MIG
#from graphviz import Graph
#import PathTraversal as draw

adjacency=dict()


def Substitution(network, node):
	if(node.nodeType!="MIG"):
		return
	[u,v] = pickPI(network, node)
	#print("u = "+str(u[0].name)+" v = "+str(v[0].name))
	old = network.nodeNum
	newN = network.clone(network.nodeNum)
	replace(network, u, v, False)
	replace(newN, u, v, True)
	network.combine(newN)
	newTop = network.getNode(node.name+old)
	network.nodeNum = network.nodeNum+node.name
	newNodeTop = dataStructure.createNode(network.nodeNum+3, "MIG", node.level+2)
	newNodeLeft = dataStructure.createNode(network.nodeNum+2, "MIG", node.level+1)
	newNodeRight = dataStructure.createNode(network.nodeNum+1, "MIG", node.level+1)
	newNodeLeft.Fin = [[node,0], [u[0],'0'] , [v[0],inv(v[1])]]
	newNodeRight.Fin = [[newTop,0], [u[0],inv(u[1])] , [v[0],inv(v[1])]]
	newNodeTop.Fin = [[newNodeRight,0],[newNodeLeft,0],[v[0],0]]
	newNodeTop.Fout = node.Fout
	for i,fout in enumerate(node.Fout):
		for j,fin in enumerate(fout.Fin):
			if(fin[0].name == node.name):
				node.Fout[i].Fin[j][0] = newNodeTop
	for i,fout in enumerate(newTop.Fout):
		for j,fin in enumerate(fout.Fin):
			if(fin[0].name == newTop.name):
				newTop.Fout[i].Fin[j][0] = newNodeTop
	node.Fout = [newNodeLeft]
	newTop.Fout = [newNodeRight]
	v[0].Fout = []
	v[0].insertFout(newNodeTop)
	v[0].insertFout(newNodeLeft)
	v[0].insertFout(newNodeRight)
	u[0].insertFout(newNodeLeft)
	u[0].insertFout(newNodeRight)
	newNodeLeft.insertFout(newNodeTop)
	newNodeRight.insertFout(newNodeTop)
	network.insertNodes(newNodeRight)
	network.insertNodes(newNodeTop)
	network.insertNodes(newNodeLeft)
