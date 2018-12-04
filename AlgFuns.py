import NtkParser as parser
import pdb
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
		for n in node:
			if(n[1] == '1'):
				n[1] = '0'
			else:
				n[1] = '1'
	
	
	def index_(node,n):
		if n in node:
			return node.index
		else
			return -1
			
			
	def exchg(self,node, node_):
		for i,n in enumerate(node.Fout):
			for j,in_node in enumerate(n.Fin):
				if(in_node[0].name == node.name):
					node.Fout[i].Fin[j] = node_