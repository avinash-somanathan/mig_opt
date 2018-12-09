# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:03:59 2018

@author: abhay
"""
import parserNetwork
import MIG
import associativity as A
import pdb
import critical_parser as crit
import PathTraversal as draw
#from PathTraversal import draw_graph as drawGrp

parserNetwork.parser("networkOut.out")

MIG.convToMIG(parserNetwork.pNtk)

dupNtk = parserNetwork.pNtk.copy()



dupNtk.PI
pdb.set_trace()
dic = crit.levelizeNodes(parserNetwork.pNtk)

for key in dic.keys():
	print "------------------------------"
	print "level -> "+str(key)
	for node in dic[key]:
		print node.name

x,y,adj = draw.create_adjacency(parserNetwork.pNtk)
draw.draw_graph(adj)
pdb.set_trace()
#parserNetwork.pNtk.printNodes()
print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(11)))
A.associativity(parserNetwork.pNtk ,parserNetwork.pNtk.getNode(4), "")

print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(11)))