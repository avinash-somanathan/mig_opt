# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:21:04 2018

@author: abhay
"""
import pdb
from dataStructure import createNode

def convToMIG(cNetwork):
	for eachNode in cNetwork.nodes.keys():
		if cNetwork.nodes[eachNode].nodeType == "AND" or (cNetwork.nodes[eachNode].nodeType == "Output" and len(cNetwork.nodes[eachNode].Fin)>1):
			newNode = createNode(cNetwork.nextNode, "CONST", (cNetwork.nodes[eachNode].level)+1)
			newNode.setValue(0)
			newNode.insertFout(cNetwork.nodes[eachNode])
			cNetwork.insertNodes(newNode)
			if not cNetwork.nodes[eachNode].nodeType == "Output":
				cNetwork.nodes[eachNode].nodeType = "MIG"
			cNetwork.nodes[eachNode].insertFin([newNode,'0'])
	return 
			