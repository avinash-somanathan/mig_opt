import AlgFuns as fun
import associativity
import substitution
import dataStructure
import parserNetwork
import pdb
import MIG
import critical_parser
import PathTraversal as draw
import random
import sys

def optimize(network, effort):
	old = network.cloneFull()
	old2 = old.cloneFull()
	critical_parser.levelizeNodes(network)
	i = 0
	while(i<effort):
		try:
			done = True
			if(len(network.nodes)<len(old.nodes)):
				print(len(network.nodes))
				print(len(old.nodes))
				old = network.cloneFull()
				old2 = old.cloneFull()
			for v in network.nodes.values():
				if(v.nodeType == "MIG"):
					fun.Majority(network,v)
					fun.Distributive(network,v)
					if(v.level >= 3):
						associativity.associativity(network,v,"NO")
						associativity.associativity(network,v,"COMP")
						#fun.Relevance(network,v)
			secure_random = random.SystemRandom()
			try:
				substitution.Substitution(network,network.PO[0].Fin[0][0])
			except Exception as e:
				pass
			for v in network.nodes.values():
				if(v.nodeType == "MIG"):
					fun.Majority(network,v)
					#fun.Distributive(network,v)
			i = i+1
			critical_parser.levelizeNodes(network)
			# if(len(network.nodes)>len(old.nodes)):
				# network = old.cloneFull()
		except Exception as e:
			i = i+1
	return old
	
			