class network:
    def __init__(self):
        self.nodes = list();
        
    def insertNodes(self, node):
        self.nodes.append(node)
    
    def printNodes(self):
        for node in self.nodes:
            print (node.name+" "+str(node.Fin)+" "+str(node.Fout))
            
    def exists(self, searchNode):
        for node in self.nodes:
            if(node.name == searchNode):
                return True, node
        return False , None
        
class node:
    def __init__(self, name, nodeType):
        self.name = name
        self.nodeType = nodeType;
        self.Fin = list()
        self.Fout = list()
        self.value = 0
        self.level = 0
        
    def insertFin(self, finNode):
        self.Fin.append(finNode)
        
    def insertFout(self, foutNode):
        self.Fout.append(foutNode)
    
    def setValue(self, val):
        self.value = val
    
    def setLevel(self, level):
        self.level = level
        
file = open("networkOut.out",'r')

pNtk = network()

for line in file:
    if "Primary" in line:
        Id = line.split(':')[1].strip().split(' ')
        for name in Id:
            if "input" in line:
                newNode = node(name, "Input")
            else:
                newNode = node(name, "Output")
                
            pNtk.insertNodes(newNode)
    
    else:
        nodeDet = line.strip().split(':')
        if nodeDet[0] == "0":
            continue
        else:
            (exist, tempNode) = pNtk.exists(nodeDet[0])
            if not exist:
                tempNode = node(nodeDet[0], "Node")
                
            if nodeDet[1] != None:
                for fin in nodeDet[1].strip().split(' '):
                   tempNode.insertFin(fin.split('-')[0])

            if nodeDet[2] != None:
                for fout in nodeDet[2].strip().split(' '):
                    tempNode.insertFout(fout.split('-')[0])
            if not exist:
                pNtk.insertNodes(tempNode)
               
print(pNtk.printNodes())