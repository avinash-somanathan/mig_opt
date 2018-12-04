import NtkParser as parser
import AlgFuns as fun
import pdb
if __name__=='__main__':
	pNtk=parser.network()
	pNtk.PI.append(0)
	newNode=parser.node(0,'x',"Input",0)
	pNtk.insertNodes(newNode)
	pNtk.PI.append(1)
	newNode=parser.node(1,'y',"Input",0)
	pNtk.insertNodes(newNode)
	pNtk.PI.append(2)
	newNode=parser.node(2,'z',"Input",0)
	pNtk.insertNodes(newNode)
	pNtk.PI.append(3)
	newNode=parser.node(3,'w',"Input",0)
	pNtk.insertNodes(newNode)
	
	newNode=parser.node(4,'a',"AND",1)
	newNode.insertFin(pNtk.getNode(0))
	newNode.insertFin(pNtk.getNode(0))
	newNode.insertFin(pNtk.getNode(1))
	pNtk.getNode(0).insertFout(newNode)
	pNtk.getNode(1).insertFout(newNode)
	pNtk.insertNodes(newNode)
	
	newNode=parser.node(5,'b',"AND",2)
	newNode.insertFin(pNtk.getNode(2))
	newNode.insertFin(pNtk.getNode(1))
	newNode.insertFin(pNtk.getNode(4))
	pNtk.getNode(4).insertFout(newNode)
	pNtk.getNode(1).insertFout(newNode)
	pNtk.getNode(2).insertFout(newNode)
	pNtk.insertNodes(newNode)
	print("Nodes currently present :"+str(pNtk.numberOfNodes()))
	fun.AlgFuns().Majority(pNtk, pNtk.getNode(4))
	print("Nodes reduced after Majority :"+str(pNtk.numberOfNodes()))
	fun.AlgFuns().Inversion(pNtk,pNtk.getNode(5))
	print("After Adding inversion logic to node5 number of nodes :"+str(pNtk.numberOfNodes()))
	
	