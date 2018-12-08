
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