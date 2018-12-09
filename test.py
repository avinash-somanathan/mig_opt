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

parserNetwork.parser("networkOut.out")
MIG.convToMIG(parserNetwork.pNtk)

#pdb.set_trace()
dic = crit.levelizeNodes(parserNetwork.pNtk)

print(dic.keys())

#parserNetwork.pNtk.printNodes()
print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(6)))
A.associativity(parserNetwork.pNtk ,parserNetwork.pNtk.getNode(6), "")

print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(6)))