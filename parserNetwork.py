from dataStructure import network
from dataStructure import node
        
pNtk = network()
        
def parser(fileName):        
    file = open(fileName,'r')
    
    
    
    for line in file:
        if "Primary" in line:
            Id = line.split(':')[1].strip().split(' ')
            for name in Id:
                if "input" in line:
                    pNtk.PI.append(name)
                    newNode = node(name, "Input", 0)
                else:
                    pNtk.PO.append(name)
                    newNode = node(name, "Output", 0)
                    
                pNtk.insertNodes(newNode)
        
        else:
            nodeDet = line.strip().split(':')
            if nodeDet[0] == "0":
                continue
            else:
                (exist, tempNode) = pNtk.exists(nodeDet[0])
                if not exist:
                    tempNode = node(nodeDet[0], "AND", int(nodeDet[3]))
                else:
                    tempNode.setLevel(int(nodeDet[3]))
                if nodeDet[1] != '':                   
                    for fin in nodeDet[1].strip().split(' '):
                        nodeExist, finNode = pNtk.exists(fin.split('-')[0])
                        if(not nodeExist):
                            finNode = node(fin.split('-')[0], "AND", 0)
                            pNtk.insertNodes(finNode)
                            
                        tempNode.insertFin([pNtk.getNode(fin.split('-')[0]), fin.split('-')[1]])
    
                if nodeDet[2] != '':
                    for fout in nodeDet[2].strip().split(' '):
                        nodeExist, foutNode  = pNtk.exists(fout.split('-')[0])
                        if(not nodeExist):
                            foutNode = node(fout.split('-')[0], "AND", 0)
                            pNtk.insertNodes(foutNode)
                        
                        tempNode.insertFout(pNtk.getNode(fout.split('-')[0]))
                if not exist:
                    pNtk.insertNodes(tempNode)
    file.close()              