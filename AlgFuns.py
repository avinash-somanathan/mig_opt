import NtkParser as parser
import pdb
from dataStructure import createNode
class AlgFuns:
	def __init__(self):
		pass
	
	def Majority(self,network,node):
		for i,fin in enumerate(node.Fin):
			cur0 = node.Fin[i%3]
			cur1 = node.Fin[(i+1)%3]
			cur2 = node.Fin[(i+2)%3]
			if (cur0[0].name == cur1[0].name):
				pdb.set_trace()
				if(cur0[1] == cur1[1]):
					self.exchg(node, cur1)
				else:
					self.exchg(node, cur2)
				network.deleteNode(node.name)
				break
				
	def Inversion(self,network,node):
		for n in node.Fin:
			if(n[1] == '1'):
				n[1] = '0'
			else:
				n[1] = '1'

	def Distributive(self, network, node):
		indexes = []
		flag = false
		i = 0
		for i,n in enumerate(node.Fin):
			indexes = []
			for j,n_ in enumerate(n[0].Fin):
				indexes.append(index_(node.Fin[(i+1)%3].Fin, n_))
			if(sum([1 for k in x if k == -1]) <= 1):
				flag = True
				break
		if(flag == True):
			firstMatch = indexes.index(-1)
			node.Fin[i] = node.Fin[i][0].Fin[firstMatch-1]
			node.Fin[(i+1)%3] = node.Fin[i][0].Fin[firstMatch-2]
			newNode = createNode(network.nodeNum+1, "MIG", node.level-1)
			newNode.insertFin(node.Fin[i][0].Fin[indexes.index(-1)])
			a = range(3)
			newNode.insertFin(node.Fin[(i+1)%3][0].Fin[[k for k in a if k not in x][0]])
			node.Fin[(i+2)%3] = [newNode , '0']
			
				
			
	def index_(node,n):
		if n in node:
			return node.index(n)
		else
			return -1
			
			
	def exchg(self,node, node_):
		for i,n in enumerate(node.Fout):
			for j,in_node in enumerate(n.Fin):
				if(in_node[0].name == node.name):
					node.Fout[i].Fin[j] = node_