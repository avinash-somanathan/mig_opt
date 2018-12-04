# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:03:59 2018

@author: abhay
"""
import parserNetwork
import MIG


parserNetwork.parser("networkOut.out")

MIG.convToMIG(parserNetwork.pNtk)
parserNetwork.pNtk.printNodes()



