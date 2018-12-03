import NtkParser as parser
import AlgFuns as fun
import pdb
if __name__=='__main__':
	pNtk=parser.network()
	pNtk.PI.append(0)
	newNode=parser.node(0,"Input",0)
	pNtk.insertNodes(newNode)
	pNtk.PI.append(1)
	newNode=parser.node(1,"Input",0)
	pNtk.insertNodes(newNode)
	pNtk.PI.append(2)
	newNode=parser.node(2,"Input",0)
	pNtk.insertNodes(newNode)
	pNtk.PI.append(3)
	newNode=parser.node(3,"Input",0)
	pNtk.insertNodes(newNode)
	
	newNode=parser.node(4,"AND",1)
	newNode.insertFin(pNtk.getNode(0))
	newNode.insertFin(pNtk.getNode(0))
	newNode.insertFin(pNtk.getNode(1))
	pNtk.insertNodes(newNode)
	
	newNode=parser.node(5,"AND",2)
	newNode.insertFin(pNtk.getNode(2))
	newNode.insertFin(pNtk.getNode(1))
	newNode.insertFin(pNtk.getNode(4))
	pNtk.getNode(4).insertFout(newNode)
	pNtk.insertNodes(newNode)
	pNtk.numberOfNodes()
	fun.AlgFuns().Majority(pNtk, pNtk.getNode(4))
	pNtk.numberOfNodes()
	
	