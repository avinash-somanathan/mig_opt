# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:03:59 2018

@author: abhay
"""
import parser
import MIG


parser.parser("networkOut.out")

MIG.convToMIG(parser.pNtk)
parser.pNtk.printNodes()



