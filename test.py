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
import critical_finder as insertError
import dataStructure as ds
import wrapper as alg
#from PathTraversal import draw_graph as drawGrp

parserNetwork.parser("networkOut.out")

MIG.convToMIG(parserNetwork.pNtk)

#pdb.set_trace()
dic = crit.levelizeNodes(parserNetwork.pNtk)

dupNtkA = parserNetwork.pNtk.copy()
dupNtkB = parserNetwork.pNtk.copy()
dupNtkC = parserNetwork.pNtk.copy()

x,y,adj = draw.create_adjacency(dupNtkA)
draw.draw_graph(adj)

pdb.set_trace()

critVoters = insertError.find_connected_nodes(parserNetwork.pNtk)

insertError.introduce_error_wrapper(critVoters, dupNtkA, dupNtkB, dupNtkC)

#optimize each ntk
alg.optimize(dupNtkA, 100)
alg.optimize(dupNtkB, 100)
alg.optimize(dupNtkC, 100)


x,y,adj = draw.create_adjacency(dupNtkA)
draw.draw_graph(adj)

pdb.set_trace()

x,y,adj = draw.create_adjacency(dupNtkB)
draw.draw_graph(adj)

pdb.set_trace()

x,y,adj = draw.create_adjacency(dupNtkC)
draw.draw_graph(adj)

pdb.set_trace()

networkList = [dupNtkA, dupNtkB, dupNtkC]
for x in networkList:
	crit.levelizeNodes(x)

finalNtk = ds.network()
outNode = ds.createNode(finalNtk.nextNode, "output", 0)
constNode = ds.createNode(0, "CONST", 0)
constNode.value = 0
finalNtk.insertNodes(outNode)
finalNtk.PO.append(outNode)
finalNtk.insertNodes(outNode)



for ntk in networkList:
	pdb.set_trace()
	if len(ntk.PO[0].Fin) > 1:
		finalNtk.mergeNetwork(ntk, [ntk.PO[0], '0'])
	else:
		finalNtk.mergeNetwork(ntk, ntk.PO[0].Fin[0])

	x,y,adj = draw.create_adjacency(finalNtk)
	draw.draw_graph(adj)


pdb.set_trace()

alg.optimize(finalNtk, 100)

x,y,adj = draw.create_adjacency(finalNtk)
draw.draw_graph(adj)


