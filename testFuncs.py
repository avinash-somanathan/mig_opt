import NtkParser as parser
import AlgFuns as fun
import parserNetwork
import MIG


parserNetwork.parser("networkTest.out")

MIG.convToMIG(parserNetwork.pNtk)
parserNetwork.pNtk.printNodes()
print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(5)))
fun.AlgFuns().Majority(parserNetwork.pNtk, parserNetwork.pNtk.getNode(4))
print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(5)))
#fun.AlgFuns().Inversion(pNtk,pNtk.getNode(5))

