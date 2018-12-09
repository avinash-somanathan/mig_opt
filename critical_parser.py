import pdb
def dependentNodes(file):
	file = open(file)
	
	nodeDict = dict()
	
	for line in file:
		line = line.replace('[', '')
		line = line.replace(']', '')
		nodeList = line.strip().split(',')
	
		if not nodeList[0] in nodeDict.keys():
			nodeDict[nodeList[0]] = set()
		
		for x in range(1, len(nodeList)-1):
			nodeDict[nodeList[0]].add(nodeList[x].strip())
	return nodeDict


levelized = list()

def levelizeNodes(pNtk):
	nodesLevel = dict()

	for nodes in pNtk.PI:
		nodes.setLevel(0)
		if not 0 in nodesLevel.keys(): 
			nodesLevel[0] = list()
		nodesLevel[0].append(nodes)

		levelized.append(int(nodes.name))
	for node in pNtk.nodes.keys():
		if not node in levelized:
			levelize(pNtk, pNtk.getNode(node), nodesLevel) 
	return nodesLevel

def levelize(pNtk, node, nodesLevel):
	levels = list()
	if not node.nodeType == "CONST":
		for inputs in node.Fin:
			#pdb.set_trace()
			if int(inputs[0].name) in levelized:
				levels.append(inputs[0].level)
			else:
				levelize(pNtk, inputs[0], nodesLevel)
				levels.append(inputs[0].level)

			node.level = max(levels)+1
	else:
		node.level = 0

	
	if not node.level in nodesLevel.keys(): 
		nodesLevel[node.level] = list()


	if not int(node.name) in levelized:		
		nodesLevel[node.level].append(node)

	levelized.append(int(node.name))