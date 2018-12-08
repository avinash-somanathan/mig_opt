import pdb
import random
from dataStructure import createNode

def swap(net1, net2, net1TopNode, net2TopNode):
	index = net1TopNode.Fin.index(net1)
	net1TopNode.Fin.remove(net1)
	net1TopNode.Fin.insert(index,net2)

	index = net2TopNode.Fin.index(net2)
	net2TopNode.Fin.remove(net2)
	net2TopNode.Fin.insert(index, net1)

	index = net1[0].Fout.index(net1TopNode)
	net1[0].Fout.remove(net1TopNode)
	net1[0].Fout.insert(index, net2TopNode)

	index = net2[0].Fout.index(net2TopNode)
	net2[0].Fout.remove(net2TopNode)
	net2[0].Fout.insert(index, net1TopNode)


def replace(net1, net2, topNode):
	index = topNode.Fin.index(net2)
	topNode.Fin.remove(net2)
	topNode.Fin.insert(index,net1)

	index = net2[0].Fout.index(topNode)
	net2[0].Fout.remove(topNode)
	net1[0].Fout.insert(index, topNode)


def associativity(cNetwork, node, comp):
	#pdb.set_trace()
	#fan-ins of the current node
	fins = [x for x in [node.Fin[y] for y in range(len(node.Fin))]]

	#checking for majority Nodes
	#choice gives the index of the fanins which has Maj node 
	choice = [y for y in range(len(fins)) if (fins[y][0].nodeType == "AND")]
	#pdb.set_trace()
	

	applyNode = None
	commonNode = None
	compNet = None

	for everyMaj in choice:
		nextFins = fins[everyMaj][0].Fin
		for other in fins:
			#pdb.set_trace()
			newNet = [x for x in other]
			if("COMP" in comp.upper()):
				newNet[1] = str(abs((int(newNet[1])-1)))
			if other!=fins[everyMaj]:
				#pdb.set_trace()
				if newNet in nextFins:
					applyNode = fins[everyMaj]
					commonNode = newNet
					compNet = other
					break
		if(applyNode != None):
			break

	if applyNode != None:
		nextFins = applyNode[0].Fin
		if "COMP" in comp.upper():
			swapChoice = [x for x in fins if (x!=compNet and x!=applyNode)]
		else:
			swapChoice = [x for x in nextFins if x!=commonNode]

		curFin = [x for x in fins if (x!=applyNode or x!=commonNode)][0]
		#pdb.set_trace()
		if "COMP" in comp.upper():
			#replace(swapChoice[0], commonNode, )
			replace(swapChoice[0], commonNode, applyNode[0])
		else:
			swap(swapChoice[0], curFin, applyNode[0], node)


	return cNetwork