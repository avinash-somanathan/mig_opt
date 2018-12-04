import NtkParser as parser
class AlgFuns:
	def __init__(self):
		pass
	
	def Majority(self,network,node):
		for i,fin in enumerate(node.Fin):
			cur0 = node.Fin[i%3]
			cur1 = node.Fin[(i+1)%3]
			cur2 = node.Fin[(i+2)%3]
			if (cur0.literal == cur1.literal):
				if(cur0.nodeType == cur1.nodeType):
					self.exchg(node, cur1)
				else:
					self.exchg(node, cur2)
				network.deleteNode(node.name)
				break
				
	def Inversion(self,network,node):
		for i,fin in reversed(list(enumerate(node.Fin))):
			newNode = parser.node(network.numberOfNodes()+1, fin.literal, "INV", node.level-1)
			node.Fin[i] = newNode
			network.insertNodes(newNode)
			
			
	def exchg(self,node, node_):
		for n in node.Fout:
			for in_node in n.Fin:
				if(in_node.name == node.name):
					in_node = node_