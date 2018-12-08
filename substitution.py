##################################
### author: Avinash Somanathan ###
##################################


from random import randrange
import dataStructure
import parserNetwork
import pdb
from graphviz import Graph

adjacency=dict()


def Substitution(network, node):
	[u,v] = pickPI(network, node)
	newTop = duplicate_net_start(network, node)
	pdb.set_trace()
	newNodeTop = dataStructure.createNode(network.nodeNum+3, "MIG", node.level+2)
	newNodeLeft = dataStructure.createNode(network.nodeNum+2, "MIG", node.level+1)
	newNodeRight = dataStructure.createNode(network.nodeNum+1, "MIG", node.level+1)
	newNodeLeft.insertFin([[node,0], u , [v[0],inv(v[1])]])
	newNodeRight.insertFin([[newTop,0], [u[0],inv(u[1])] , [v[0],inv(v[1])]])
	newNodeTop.insertFin([[newNodeRight,0],[newNodeLeft,0],v])
	newNodeLeft.insertFout(newNodeTop)
	newNodeRight.insertFout(newNodeTop)
	network.insertNodes(newNodeRight)
	network.insertNodes(newNodeTop)
	network.insertNodes(newNodeLeft)
	print newNodeTop,newNodeTop,newNodeLeft
	pdb.set_trace()
	recursive_replace(node, network, u, v)
	recursive_replace(newTop, network, [u[0],inv(u[1])], v)
	

	

def inv(i):
	if i=='0':
		return '1'
	else:
		return '0'

def pickPI( network, node):
	rand_index = randrange(len(network.PI)-1)
	u = [network.getNode(network.PI[rand_index]),0]			#pick a randm input
	v = [network.getNode(network.PI[rand_index+1]),0]			#use circular feature in python
	pdb.set_trace()
	return [u,v]
def duplicate_net_start(network,node):
	nodeNumold=network.nodeNum
	newNode = dataStructure.createNode(nodeNumold + node.name, "MIG", node.level)
	newNodeTopm1 = duplicate_net(network,node)
	for f in node.Fin:
		newNode.insertFin([network.getNode(f[0].name+nodeNumold),f[1]])
	return newNode


def duplicate_net( network, node):   #need to complete this def
	nodeNumold=network.nodeNum
	for i,fin in enumerate(node.Fin):
		if fin[0].nodeType != "Input":
			newNode = dataStructure.createNode(nodeNumold + fin[0].name, "MIG", fin[0].level)
			network.insertNodes(newNode)
			duplicate_net(network, fin[0])
			for f in fin[0].Fin:
				newNode.insertFin([network.getNode(f[0].name+nodeNumold),f[1]])
			for fo in fin[0].Fout:
				newNode.insertFout(network.getNode(fo.name+nodeNumold))
			return newNode
def recursive_replace( node, network, u, v):
	for fin in node.Fin:
		pdb.set_trace()
		if fin[0].name == v[0].name and int(fin[1]) == v[1]:
			fin[0].name = u[0].name
			if fin[0].nodeType != "Input":
				recursive_replace( fin, network, u, v)

def create_adjacency(network):
	pi = list()
	po = list()
	for node in network.nodes.keys():
        	edges = list()
        	for i in range(0,len(network.nodes[node].Fout)):
                	edges.append(network.nodes[node].Fout[i].name)
	        if network.nodes[node].nodeType == "Input":
        		pi.append(network.nodes[node].name)
		if network.nodes[node].nodeType == "Output":
            		po.append(network.nodes[node].name)
	        adjacency[node] = edges
	return pi,po,adjacency


def draw_graph(adjacency):
	g = Graph('G',filename = 'Boolean_Network')
	for node in adjacency:
		for Fout in adjacency[node]:
            #print str(node) + " " + str(Fout)
			g.edge(str(node),str(Fout))
	g.view()



parserNetwork.parser("networkTest2.out")
Substitution(parserNetwork.pNtk,parserNetwork.pNtk.getNode(9))
			
parserNetwork.pNtk.printNodes()

#pi,po,adj=create_adjacency(parserNetwork.pNtk)
#draw_graph(adj)
