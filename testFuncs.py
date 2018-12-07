import NtkParser as parser
import AlgFuns as fun
import parserNetwork
import MIG, pdb


parserNetwork.parser("networkRelevance.out")

#MIG.convToMIG(parserNetwork.pNtk)
parserNetwork.pNtk.printNodes()
print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(8)))
#fun.AlgFuns().Distributive(parserNetwork.pNtk, parserNetwork.pNtk.getNode(8))
fun.AlgFuns().Relevance(parserNetwork.pNtk, parserNetwork.pNtk.getNode(7))
print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(8)))

flag = True
while(flag):
	flag = False
	for k,v in parserNetwork.pNtk.nodes.items():
		f = fun.AlgFuns().Majority(parserNetwork.pNtk, v)
		print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(8)))
		if(f):
			flag = f
#fun.AlgFuns().Inversion(pNtk,pNtk.getNode(5))

