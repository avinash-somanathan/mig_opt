# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 23:57:49 2018

@author: abhay
"""

class network:
    def __init__(self):
        self.PI = list()
        self.PO = list()
        self.nodes = dict()
        self.nodesLevel = dict()
        self.nodeNum = 0
        self.maxLevel = 0
        self.nextNode = 1
        
    def insertNodes(self, node):
        self.nodes[node.name] = node
        self.nextNode = self.nextNode+1
        
        if node.level > self.maxLevel:
            self.maxLevel = node.level
                
        
        if not self.nodesLevel.has_key(node.level):
            self.nodesLevel[node.level] = list()
            
        self.nodesLevel[node.level].append(node)
        
        if(node.nodeType != "CONST"):
            self.nodeNum = self.nodeNum + 1;
            
    
    def printNodes(self):
        keys = self.nodes.keys()
        keys.sort()
        for node in keys:
            #print (str(self.nodes[node].name)+" "+str(self.nodes[node].Fin)+" "+str(self.nodes[node].Fout)+" "+str(self.nodes[node].level)+" "+str(self.nodes[node].nodeType))
            print ('{0:5} {1:70} {2:30} {3:20} {4:10}'.format(self.nodes[node].name, self.nodes[node].Fin, self.nodes[node].Fout, self.nodes[node].level, self.nodes[node].nodeType))
            #print(f'{keys:5} keys')
        return
            
    def exists(self, searchNode):
        if self.nodes.has_key(int(searchNode)):
            return True, self.nodes[int(searchNode)]
        return False , None              
        
        
    def numberOfNodes(self):
        print (self.nodeNum);
        return
        
    def getNode(self, name):
        if self.nodes.has_key(int(name)):
            return self.nodes[int(name)]
    
    def printNodesExt(self,node):
		if(node.nodeType == 'AND'):
			s = 'Maj('+self.printNodesExt(node.Fin[0])+', '+self.printNodesExt(node.Fin[1])+', '+self.printNodesExt(node.Fin[2])+')'
		elif(node.nodeType == 'INV'):
			s = 'INV('+self.printNodesExt(node.Fin[0])+')'
		else:
			s = node.literal
		
		return s
        
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

def createNode(name, nodeType, level):
    return node(name, nodeType, level)