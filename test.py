# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:03:59 2018

@author: abhay
"""
import parserNetwork
import MIG
import associativity as A
import pdb

parserNetwork.parser("networkTest2.out")

#MIG.convToMIG(parserNetwork.pNtk)
#parserNetwork.pNtk.printNodes()
#pdb.set_trace()
print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(6)))
A.associativity(parserNetwork.pNtk ,parserNetwork.pNtk.getNode(6), "")

print(parserNetwork.pNtk.printNodesExt(parserNetwork.pNtk.getNode(6)))