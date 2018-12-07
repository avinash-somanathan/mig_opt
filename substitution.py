##################################
### author: Avinash Somanathan ###
##################################


from random import randrange

def Substitution(self, network, node)
	[u,v] = pickPI(network, node)
	duplicate_net(network, node)
	newNode = createNode(network.nodeNum*2+1, "MIG", node.level+1)
	recursive_replace(node, network, u, v)
	recursive_replace(newDupNode, newNet, [u[0],inv(u[1])])
	newNode.insertFin(
	newNode.Fin[1] = v
	newNode.Fin[2] = newNet


def pickPI(self, network, node)
	rand_index = randrange(len(network.PI))
	u = netowrk.PI[rand_index]			#pick a randm input
	v = network.PI[rand_index+1]			#use circular feature in python
	return [u,v]

def duplicate_net(self, network, node)   #need to complete this def
	for i,fin in enumerate(node.Fin):
		if fin.nodeType != "Input"
			newNode = createNode(network.nodeNum + fin.name, "MIG", fin.level)
			duplicate_net(network, fin)
		for f in fin.Fin:
			newNode.insertFin(self.getNode(f.name+network.nodeNum))
			
def recursive_replace(self, node, network, u, v)
	for fin in node.Fin:
		if fin[0].name == u[0].name and fin[1] == u[1]:
			fin[0].name = v.name
			if fin.nodeType != "Input"
				recursive_replace(self, fin, u, v)
			
