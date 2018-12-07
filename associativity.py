import pdb
import random
from dataStructure import createNode

def swap(net1, net2, net1TopNode, net2TopNode):
	net1TopNode.Fin.remove(net1)
	net1TopNode.Fin.append(net2)
	net2TopNode.Fin.remove(net2)
	net2TopNode.Fin.append(net1)

	net1[0].Fout.remove(net1TopNode)
	net2[0].Fout.remove(net2TopNode)

	net2[0].Fout.append(net2TopNode)
	net1[0].Fout.append(net1TopNode)



def associativity(cNetwork, node):
	#pdb.set_trace()
	fins = [x for x in [node.Fin[y] for y in range(len(node.Fin))]]
	choice = [y for y in range(len(fins)) if (fins[y][0].nodeType == "AND")]
	pdb.set_trace()
	#choice gives the index of the fanins which has Maj node 

	applyNode = None
	commonNode = None

	for everyMaj in choice:
		nextFins = fins[everyMaj][0].Fin
		for other in fins:
			if other!=fins[everyMaj]:
				#pdb.set_trace()
				if other in nextFins:
					applyNode = fins[everyMaj]
					commonNode = other
					break
		if(applyNode != None):
			break

	if applyNode != None:
		nextFins = applyNode[0].Fin
		swapChoice = [x for x in nextFins if x!=commonNode]
		curFin = [x for x in fins if (x!=applyNode or x!=commonNode)][0]
		pdb.set_trace()
		swap(swapChoice[0], curFin, applyNode[0], node)


	return cNetwork