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
		n = createNode(0, "CONST", 0)
		n.setValue(0)
		self.insertNodes(n)
		
	def insertNodes(self, node):
		self.nodes[node.name] = node
		self.nextNode = self.nextNode+1
		
		if node.level > self.maxLevel:
			self.maxLevel = node.level
		
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
		for node in keys:
			print ('{0:5} {1:70} {2:30} {3:20} {4:10}'.format(self.nodes[node].name, self.nodes[node].Fin, self.nodes[node].Fout, self.nodes[node].level, self.nodes[node].nodeType))
		return
			
	def exists(self, searchNode):
		if int(searchNode) in self.nodes:
			return True, self.nodes[int(searchNode)]
		return False , None			  
		
		
	def numberOfNodes(self):
		return self.nodeNum
		
	def getNode(self, name):
		try:
			if int(name) in self.nodes:
				return self.nodes[int(name)]
		except:
			pdb.set_trace()
	
	def printNodesExt(self,node):
		try:
			if(node.nodeType == 'Output' and len(node.Fin) == 1):
				s="INV("+self.printNodesExt(node.Fin[0][0])+")"
			elif(node.nodeType != 'CONST' and node.nodeType != 'Input'):
				s = 'MAJ('+self.printNodesExt(node.Fin[0][0])
				if(str(node.Fin[0][1]) == '1'):
					s = s+"'"
				s = s+', '+self.printNodesExt(node.Fin[1][0]) 
				if(str(node.Fin[1][1]) == '1'):
					s = s+"'"
				s = s+ ', '+self.printNodesExt(node.Fin[2][0])
				if(str(node.Fin[2][1]) == '1'):
					s = s+"'"
				s = s+')'
			else:
				s = str(node.name)
			return s
		except:
			pdb.set_trace()
		
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

	def cloneFull(self):
		newNetwork = network()
		newNetwork.PI=self.PI
		newNetwork.PO=self.PO
		for n in self.nodes.values():
			newNetwork.insertNodes(n.duplicateNode(n.name))
		for k,n in newNetwork.nodes.items():
			for i,fin in enumerate(n.Fin):
				newNetwork.nodes[k].Fin[i] = [newNetwork.nodes[fin[0].name],fin[1]]
			for i,fout in enumerate(n.Fout):
				newNetwork.nodes[k].Fout[i] = newNetwork.nodes[fout.name]
		return newNetwork
		
	def clone(self, skip):
		newNetwork = network()
		newNetwork.PI=self.PI
		for n in self.nodes.values():
			if n.nodeType == 'MIG':
				newNetwork.insertNodes(n.duplicateNode(n.name+skip))
			else:
				newNetwork.insertNodes(n.duplicateNode(n.name))
		for k,n in newNetwork.nodes.items():
			for i,fin in enumerate(n.Fin):
				if fin[0].nodeType != 'Input' and fin[0].nodeType != 'CONST':
					newNetwork.nodes[k].Fin[i] = [newNetwork.nodes[fin[0].name+skip],fin[1]]
			for i,fout in enumerate(n.Fout):
				if fout.nodeType != 'Output':
					try:
						newNetwork.nodes[k].Fout[i] = newNetwork.nodes[fout.name+skip]
					except:
						pdb.set_trace()

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
		newNode.value = self.value
		return newNode

def createNode(name, nodeType, level):
	return node(name, nodeType, level)
