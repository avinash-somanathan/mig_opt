import NtkParser as parser
import pdb
from dataStructure import createNode
import PathTraversal as draw

majorityDone = []

def Majority(network, node):
	flag = False
	if not ((node.nodeType == 'Output') or (node.nodeType == 'Input')):
		#pdb.set_trace()
#		for i,fin in enumerate(node.Fin):
		finListDup = [x for x in node.Fin]
		for i,checkFin in enumerate(finListDup):
			for j,origFin in enumerate(node.Fin):
				if not i == j:
					if checkFin[0].baseName == origFin[0].baseName:
						exchg(node, origFin)
						network.deleteNode(node.name)
						applyN = node.Fout
						
						majorityDone.append(node)
						del node
						for fout in applyN:
							if fout.name in network.nodes.keys():
								#print("Removed node "+str(node.name))
								#pdb.set_trace()
								Majority(network, fout)
								
						flag = True
						break
			if flag:
				break

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

def RelevanceHelper(nodeA, nodeB, nodeC):
	flag = False
	for j,f in enumerate(nodeA[0].Fin):
		if(f[0].baseName == nodeB[0].baseName):
			nodeA[0].Fin[j] = [nodeC[0], inv(nodeB[1])]
		else:
			RelevanceHelper(nodeA[0].Fin[j],nodeB,nodeC)
	
def inv(i):
	if i=='0':
		return '1'
	else:
		return '0'

def Distributive(network, node):
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
	if(flag == True and len(indexes)>0 and (-1 in indexes)):
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
		
		
def exchg(nodeRemove, nodeKeep):
	for fin in nodeRemove.Fin:
		try:
			fin[0].Fout.remove(nodeRemove)
		except:
			print("except") #pdb.set_trace()
			
	for fout in nodeRemove.Fout:
		nodeKeep[0].Fout.append(fout)
		for fin in fout.Fin:
			if fin[0] == nodeRemove:
				fin[0] = nodeKeep[0]
				if fin[1] == nodeKeep[1]:
					fin[1] = '0'
				else:
					fin[1] = '1'
				break

