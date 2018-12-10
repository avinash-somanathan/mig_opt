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
#from PathTraversal import draw_graph as drawGrp

parserNetwork.parser("networkOut.out")

MIG.convToMIG(parserNetwork.pNtk)

pdb.set_trace()
dic = crit.levelizeNodes(parserNetwork.pNtk)

dupNtkA = parserNetwork.pNtk.copy()
dupNtkB = parserNetwork.pNtk.copy()
dupNtkC = parserNetwork.pNtk.copy()


critVoters = insertError.find_connected_nodes(parserNetwork.pNtk)

insertError.introduce_error_wrapper(critVoters, dupNtkA, dupNtkB, dupNtkC)

#optimize each ntk

