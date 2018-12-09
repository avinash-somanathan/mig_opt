import NtkParser as parser
import pdb
from dataStructure import createNode




	
def Majority(network,node):











	print(str(node.name)+" "+network.printNodesExt(node))















	flag = False
	if(node.nodeType != 'Output'):
		for i,fin in enumerate(node.Fin):
			cur0 = node.Fin[i%3]
			cur1 = node.Fin[(i+1)%3]
			cur2 = node.Fin[(i+2)%3]


			if (cur0[0].name == cur1[0].name):





























				if(cur0[1] == cur1[1]):
					exchg(node, cur1)
				else:
					exchg(node, cur2)
				network.deleteNode(node.name)
				flag = True

				break

















	return flag
			
def Inversion(network,node):
	for n in node.Fin:

		if(n[1] == '1' or n==1):
			n[1] = '0'
		else:

			n[1] = '1'
			
def Relevance( network, node):
	fin = node.Fin;
	for i,fin in enumerate(node.Fin):
		cur0 = node.Fin[i%3]
		cur1 = node.Fin[(i+1)%3]
		cur2 = node.Fin[(i+2)%3]
		RelevanceHelper(cur0,cur1,cur2)
		# for j,f in enumerate(cur0[0].Fin):
			# if(f[0].name == cur1[0].name):
				# cur0[0].Fin[j] = [cur2[0], inv(cur1[1])]
				# break
			# if(f[0].name == cur2[0].name):
				# cur0[0].Fin[j] = [cur1[0], inv(cur2[1])]
				# break

def RelevanceHelper(nodeA, nodeB, nodeC):
	flag = False
	for j,f in enumerate(nodeA[0].Fin):
		if(f[0].name == nodeB[0].name):
			nodeA[0].Fin[j] = [nodeC[0], inv(nodeB[1])]
		else:
			RelevanceHelper(nodeA[0].Fin[j],nodeB,nodeC)
	
def inv(i):
	if i=='0':
		return '1'
	else:
		return '0'

def Distributive( network, node):
	indexes = []
	flag = False
	i_ = 0
	for i,n in enumerate(node.Fin):
		indexes = []
		for j,n_ in enumerate(n[0].Fin):
			indexes.append(index_(node.Fin[(i+1)%3][0].Fin, n_))
		if(sum([1 for k in indexes if k == -1]) <= 1):
			flag = True
			i_ = i
			break
	if(flag == True):
		temp1 = node.Fin[i];
		temp2 = node.Fin[(i+1)%3]
		firstMatch = indexes.index(-1)
		node.Fin[i] = node.Fin[i][0].Fin[firstMatch-1]
		node.Fin[(i+1)%3] = temp1[0].Fin[firstMatch-2]
		newNode = createNode(network.nodeNum+1, "MIG", node.level-1)
		newNode.insertFin(temp1[0].Fin[indexes.index(-1)])
		a = range(3)
		newNode.insertFin(temp2[0].Fin[[k for k in a if k not in indexes][0]])
		newNode.insertFin(node.Fin[(i+2)%3])
		node.Fin[(i+2)%3] = [newNode , '0']
		
			
		
def index_(node,n):
	if n in node:
		return node.index(n)
	else:
		return -1
		
		
def exchg(node, node_):
	for i,n in enumerate(node_[0].Fout):
		if(n.name == node.name):
			node_[0].Fout.remove(n)
	node_[0].Fout = node_[0].Fout +node.Fout
	for i,n in enumerate(node.Fout):
		for j,in_node in enumerate(n.Fin):
			if(in_node[0].name == node.name):
				node.Fout[i].Fin[j] = node_