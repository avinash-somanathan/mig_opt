class network:
    def __init__(self):
        self.PI = list()
        self.PO = list()
        self.nodes = dict()
        self.nodesLevel = dict()
        self.nodeNum = 0
        self.maxLevel = 0
        
    def insertNodes(self, node):
        self.nodes[node.name] = node
        
        if node.level > self.maxLevel:
            self.maxLevel = node.level
                
        
        if node.level not in self.nodesLevel:
            self.nodesLevel[node.level] = list()
            
        self.nodesLevel[node.level].append(node)
        
        if(node.nodeType != "const"):
            self.nodeNum = self.nodeNum + 1;
            
    
    def printNodes(self):
        keys = self.nodes.keys()
        keys.sort()
        for node in keys:
            print (str(self.nodes[node].name)+" "+str(self.nodes[node].Fin)+" "+str(self.nodes[node].Fout)+" "+str(self.nodes[node].level))
        return
            
    def exists(self, searchNode):
        if int(searchNode) in self.nodes:
            return True, self.nodes[int(searchNode)]
        return False , None              
        
        
    def numberOfNodes(self):
        print (self.nodeNum);
        return
		
    def deleteNode(self, name):
        if int(name) in self.nodes:
            del self.nodes[int(name)]
			self.nodeNum = self.nodeNum - 1;
        
    def getNode(self, name):
        if int(name) in self.nodes:
            return self.nodes[int(name)]
        
class node:
    def __init__(self, name, nodeType, level):
        self.name = int(name)
        self.nodeType = nodeType;
        self.Fin = list()
        self.Fout = list()
        self.value = 0
        self.level = level
        
    def insertFin(self, finNode):
        self.Fin.append(finNode)
        
    def insertFout(self, foutNode):
        self.Fout.append(foutNode)
    
    def setValue(self, val):
        self.value = val
    
    def setLevel(self, level):
        self.level = level
        
        
if __name__ == '__main__':        
    file = open("networkOut.out",'r')
    
    pNtk = network()
    
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
                if nodeDet[1] != '':
                    for fin in nodeDet[1].strip().split(' '):
                        tempNode.insertFin([fin.split('-')[0], fin.split('-')[1]])
    
                if nodeDet[2] != '':
                    for fout in nodeDet[2].strip().split(' '):
                        tempNode.insertFout(fout.split('-')[0])
                if not exist:
                    pNtk.insertNodes(tempNode)
    file.close()              
