##################################
### author: Avinash Somanathan ###
##################################


from random import randrange
import dataStructure
import parserNetwork
import pdb
import AlgFuns
import MIG
# from graphviz import Graph

adjacency=dict()


def Substitution(network, node):
	[u,v] = pickPI(network, node)
	print("u = "+str(u[0].name)+" v = "+str(v[0].name))
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
	newNodeLeft.Fin = [[node,0], u , [v[0],inv(v[1])]]
	newNodeRight.Fin = [[newTop,0], [u[0],inv(u[1])] , [v[0],inv(v[1])]]
	newNodeTop.Fin = [[newNodeRight,0],[newNodeLeft,0],v]
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
	#recursive_replace(node, network, u, v)
	#recursive_replace(newTop, network, [u[0],inv(u[1])], v)
	
def replace(network, u, v, invert):
	for k in network.nodes.keys():
		for i,fin in enumerate(network.nodes[k].Fin):
			if (fin[0].name == v[0].name):
				if(invert):
					network.nodes[k].Fin[i] = [u[0],inv(fin[1])]
				else:
					network.nodes[k].Fin[i] = [u[0],fin[1]]
			
	

def inv(i):
	if i=='0' or i==0:
		return '1'
	else:
		return '0'

def pickPI( network, node):
	rand_index = randrange(len(network.PI)-1)
	u = [network.getNode(network.PI[rand_index].name),0]			#pick a randm input
	v = [network.getNode(network.PI[rand_index+1].name),0]			#use circular feature in python
	return [u,v]

def duplicate_net_start(network,node):
	nodeNumold=network.nodeNum
	newNode = dataStructure.createNode(nodeNumold + node.name, "MIG", node.level)
	newNodeTopm1 = duplicate_net(network,node)
	# for f in node.Fin:
		# newNode.insertFin([network.getNode(f[0].name+nodeNumold),f[1]])
	return newNodeTopm1


def duplicate_net( network, node):   #need to complete this def
	nodeNumold=network.nodeNum
	pdb.set_trace()
	for i,fin in enumerate(node.Fin):
		if fin[0].nodeType != "Input":
			newNode = dataStructure.createNode(nodeNumold + fin[0].name, "MIG", fin[0].level)
			network.insertNodes(newNode)
			duplicate_net(network, fin[0])
			for f in fin[0].Fin:
				newNode.insertFin([network.getNode(f[0].name+nodeNumold),f[1]])
			for fo in fin[0].Fout:
				newNode.insertFout(network.getNode(fo.name+nodeNumold))

def recursive_replace( node, network, u, v):
	for fin in node.Fin:
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


# def draw_graph(adjacency):
	# g = Graph('G',filename = 'Boolean_Network')
	# for node in adjacency:
		# for Fout in adjacency[node]:
            # #print str(node) + " " + str(Fout)
			# g.edge(str(node),str(Fout))
	# g.view()



parserNetwork.parser("networkTest2.out")
MIG.convToMIG(parserNetwork.pNtk)
print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(4)))

Substitution(parserNetwork.pNtk,parserNetwork.pNtk.getNode(10))
pdb.set_trace()
print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(4)))
flag = True
#while(1):
flag = False
for k,v in parserNetwork.pNtk.nodes.items():
	f = AlgFuns.Majority(parserNetwork.pNtk, v)
	print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(4)))
	if(f):
		flag = f
pdb.set_trace()
#parserNetwork.pNtk.printNodes()

#pi,po,adj=create_adjacency(parserNetwork.pNtk)
#draw_graph(adj)
