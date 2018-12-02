class network:
    def __init__(self):
        self.nodes = list();
        
    def insertNodes(self, node):
        self.nodes.append(node)
    
    def printNodes(self):
        for node in self.nodes:
            print node.name
    
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
            newNode = node(name, "Input")
            pNtk.insertNodes(newNode)

            
                
pNtk.printNodes()