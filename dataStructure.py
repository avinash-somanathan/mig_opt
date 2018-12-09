# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 23:57:49 2018

@author: abhay
"""
import pdb
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
				
		
		#if not node.level in self.nodesLevel:
		#	self.nodesLevel[node.level] = list()
			
		#self.nodesLevel[node.level].append(node)
		
		if(node.nodeType != "CONST"):
			self.nodeNum = self.nodeNum + 1;
			
	def setNodeLevel(self,level,node):
	    if level in self.nodesLevel.keys():
	        self.nodesLevel[level].append(node)
	    else :
	        self.nodesLevel[level] = list()
	        self.nodesLevel[level].append(node)

	def printNodes(self):
		keys = self.nodes.keys()
		#keys.sort()
		for node in keys:
			#print (str(self.nodes[node].name)+" "+str(self.nodes[node].Fin)+" "+str(self.nodes[node].Fout)+" "+str(self.nodes[node].level)+" "+str(self.nodes[node].nodeType))
			print ('{0:5} {1:70} {2:30} {3:20} {4:10}'.format(self.nodes[node].name, self.nodes[node].Fin, self.nodes[node].Fout, self.nodes[node].level, self.nodes[node].nodeType))
			#print(f'{keys:5} keys')
		return
			
	def exists(self, searchNode):
		if int(searchNode) in self.nodes:
			return True, self.nodes[int(searchNode)]
		return False , None			  
		
		
	def numberOfNodes(self):
		return self.nodeNum
		
	def getNode(self, name):
		if int(name) in self.nodes:
			return self.nodes[int(name)]
	
	def printNodesExt(self,node):
		if(node.nodeType != 'CONST' and node.nodeType != 'Input'):
			s = 'MAJ('+self.printNodesExt(node.Fin[0][0])
			if(node.Fin[0][1] == '1'):
				s = s+"'"
			s = s+', '+self.printNodesExt(node.Fin[1][0]) 
			if(node.Fin[1][1] == '1'):
				s = s+"'"
			s = s+ ', '+self.printNodesExt(node.Fin[2][0])
			if(node.Fin[2][1] == '1'):
				s = s+"'"
			s = s+')'
		else:
			s = str(node.name)
		return s
		
	def deleteNode(self, name):
		if int(name) in self.nodes:
			del self.nodes[int(name)]
			self.nodeNum = self.nodeNum - 1;

	def copy(self):
		newNetwork = network()

		for n in self.nodes.values():
			newNetwork.insertNodes(n.duplicateNode(n.name))

		newNetwork.PI = [newNetwork.nodes[x.name] for x in self.PI]
		newNetwork.PO = [newNetwork.nodes[x.name] for x in self.PO]
	
		for k,n in newNetwork.nodes.items():
		        for i,fin in enumerate(n.Fin):
					newNetwork.nodes[k].Fin[i] = [newNetwork.nodes[fin[0].name],fin[1]]

		        for i,fout in enumerate(n.Fout):
					newNetwork.nodes[k].Fout[i] = newNetwork.nodes[fout.name]

		return newNetwork

	def clone(self, skip):
		newNetwork = network()
		newNetwork.PI = self.PI
		newNetwork.PO = self.PO

		for n in self.nodes.values():
		        if n.nodeType != 'Input' and n.nodeType != 'Output':
		                newNetwork.insertNodes(n.duplicateNode(n.name+skip))
		        else:
		                newNetwork.insertNodes(n.duplicateNode(n.name))
		for k,n in newNetwork.nodes.items():
		        for i,fin in enumerate(n.Fin):
		                if fin[0].nodeType != 'Input':
		                        newNetwork.nodes[k].Fin[i] = [newNetwork.nodes[fin[0].name+skip],fin[1]]
		        for i,fout in enumerate(n.Fout):
		                if fout.nodeType != 'Output':
		                        newNetwork.nodes[k].Fout[i] = newNetwork.nodes[fout.name+skip]
		                else:
		                        newNetwork.nodes[k].Fout[i] = newNetwork.nodes[fout.name]
		return newNetwork

	def combine(self, net):
		for k,n in net.nodes.items():
	        exists, _ = self.exists(k)
	        if(exists == True):
	                for fout in n.Fout:
	                        self.nodes[k].insertFout(fout)
	        else:
	                self.insertNodes(n)


		
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

	def duplicateNode(self, name):
		newNode = createNode(name, self.nodeType, self.level)
		newNode.Fin = list(self.Fin)
		newNode.Fout = list(self.Fout)
		return newNode

def createNode(name, nodeType, level):
	return node(name, nodeType, level)
