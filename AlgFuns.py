import NtkParser as parser
import pdb
from dataStructure import createNode
class AlgFuns:
	def __init__(self):
		pass
	
	def Majority(self,network,node):
		flag = False
		try:
			for i,fin in enumerate(node.Fin):
				cur0 = node.Fin[i%3]
				cur1 = node.Fin[(i+1)%3]
				cur2 = node.Fin[(i+2)%3]
				if (cur0[0].name == cur1[0].name):
					if(cur0[1] == cur1[1]):
						self.exchg(node, cur1)
					else:
						self.exchg(node, cur2)
					network.deleteNode(node.name)
					flag = True
					break
		except:
			pdb.set_trace()
		return flag
				
	def Inversion(self,network,node):
		for n in node.Fin:
			if(n[1] == '1'):
				n[1] = '0'
			else:
				n[1] = '1'
				
	def Relevance(self, network, node):
		fin = node.Fin;
		for i,fin in enumerate(node.Fin):
			cur0 = node.Fin[i%3]
			cur1 = node.Fin[(i+1)%3]
			cur2 = node.Fin[(i+2)%3]
			self.RelevanceHelper(cur0,cur1,cur2)
			# for j,f in enumerate(cur0[0].Fin):
				# if(f[0].name == cur1[0].name):
					# cur0[0].Fin[j] = [cur2[0], self.inv(cur1[1])]
					# break
				# if(f[0].name == cur2[0].name):
					# cur0[0].Fin[j] = [cur1[0], self.inv(cur2[1])]
					# break

	def RelevanceHelper(self,nodeA, nodeB, nodeC):
		flag = False
		for j,f in enumerate(nodeA[0].Fin):
			if(f[0].name == nodeB[0].name):
				nodeA[0].Fin[j] = [nodeC[0], self.inv(nodeB[1])]
			else:
				self.RelevanceHelper(nodeA[0].Fin[j],nodeB,nodeC)
		
	def inv(self,i):
		if i=='0':
			return '1'
		else:
			return '0'

	def Distributive(self, network, node):
		indexes = []
		flag = False
		i_ = 0
		for i,n in enumerate(node.Fin):
			indexes = []
			for j,n_ in enumerate(n[0].Fin):
				indexes.append(self.index_(node.Fin[(i+1)%3][0].Fin, n_))
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
			
	def Substitution():
		pass
			
				
			
	def index_(self,node,n):
		if n in node:
			return node.index(n)
		else:
			return -1
			
			
	def exchg(self,node, node_):
		for i,n in enumerate(node.Fout):
			for j,in_node in enumerate(n.Fin):
				if(in_node[0].name == node.name):
					node.Fout[i].Fin[j] = node_