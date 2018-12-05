import NtkParser as parser
import AlgFuns as fun
import parserNetwork
import MIG


parserNetwork.parser("networkTest2.out")

#MIG.convToMIG(parserNetwork.pNtk)
parserNetwork.pNtk.printNodes()
print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(8)))
fun.AlgFuns().Distributive(parserNetwork.pNtk, parserNetwork.pNtk.getNode(8))
print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(8)))
#fun.AlgFuns().Inversion(pNtk,pNtk.getNode(5))

