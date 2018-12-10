import dataStructure 
import parserNetwork
import PathTraversal
import operator 
import pdb


node_criticality = dict()

def Sort_Levels(network):
    
    Sorted_Level_List = dict()
    level_list = network.nodesLevel.keys()
    level_list.sort(reverse=True)
    #print level_list
    
    for level in level_list:
        Sorted_Level_List[level] = network.nodesLevel[level]
    
    return Sorted_Level_List

def find_connected_nodes(network):
    critical_voters_list = list()
    fanout_a = list()
    fanout_b = list()

    for node in network.PO:
        node_criticality[node.name] = 0
    
    Sorted_Level_List = Sort_Levels(network)

    for level in reversed(Sorted_Level_List.keys()):
        for node in range(len(Sorted_Level_List[level])):
            temp_node = Sorted_Level_List[level][node]
            criticality_fout = 0
            for node in temp_node.Fout:
                criticality_fout += node_criticality[node.name]
            criticality = float(len(temp_node.Fout))*(0.33333) + float(criticality_fout)*(0.33333)
            node_criticality[temp_node.name] = criticality
            #print "Level : %d  Node Name : %d Criticality : %.5f "%(temp_node.level,temp_node.name,criticality)
    del node_criticality[0]
    #print node_criticality
    sorted_dictionary = sorted(node_criticality.items(),key=operator.itemgetter(1),reverse=True)


    critical_voters_list.append(sorted_dictionary[0][0])
    critical_voters_list.append(sorted_dictionary[1][0])
    
    a = dataStructure.network.getNode(network,critical_voters_list[0])
    b = dataStructure.network.getNode(network,critical_voters_list[1])
    
    for node in a.Fout:
        fanout_a.append(node.name)
    
    for node in b.Fout:
        fanout_b.append(node.name)

    for iteration in range(2,len(node_criticality)):
        common_node = list(set(fanout_a)&set(fanout_b))
        if len(common_node) > 0:
            break 
        else :
            fanout_a = list()
            fanout_b = list()
            critical_voters_list.pop(0)
            critical_voters_list.append(sorted_dictionary[iteration][0])
            a = dataStructure.network.getNode(network,critical_voters_list[0])
            b = dataStructure.network.getNode(network,critical_voters_list[1])
            for node in a.Fout:
                fanout_a.append(node.name)
            for node in b.Fout:
                fanout_b.append(node.name)

            
    for node in common_node:
        critical_voters_list.append(node)

    return critical_voters_list


def introduce_error_wrapper(critical_voters_list, ntkA, ntkB, ntkC):
    voterA = critical_voters_list[0]
    voterB = critical_voters_list[1]
    commonNodes = [critical_voters_list[x] for x in range(2,len(critical_voters_list))]



    if ntkA.getNode(voterA).level <= ntkA.getNode(voterB).level :
        introduce_error([ntkA.getNode(voterB), '0'],[ntkA.getNode(voterA), '1'], ntkA)
    else:
        introduce_error([ntkA.getNode(voterA), '0'],[ntkA.getNode(voterB), '1'], ntkA)

    introduce_error([ntkB.getNode(commonNodes[0]), '0'], [ntkB.getNode(voterA), '0'], ntkB)
    introduce_error([ntkC.getNode(commonNodes[0]), '0'], [ntkC.getNode(voterB), '0'], ntkC)


def introduce_error(netA, netB, pNtk):#replace netA by netB in pNtk network
    
    x,y,adj = PathTraversal.create_adjacency(pNtk)
    PathTraversal.draw_graph(adj)

    pdb.set_trace()

    change_fanout(pNtk, netB, netA, netB[1])
    change_fanin(pNtk, netB, netA)

    for fout in netA[0].Fout:
        netB[0].Fout.append(fout)

    pNtk.deleteNode(netA[0].name)

    pdb.set_trace()

    x,y,adj = PathTraversal.create_adjacency(pNtk)
    PathTraversal.draw_graph(adj)

def change_fanout(network, netB, netA, complement):
    for fout in netA[0].Fout:
        for replace_node in fout.Fin:
            if replace_node[0].name == netA[0].name:
                replace_node[0] = netB[0]
                if complement != '0':
                    replace_node[1] = str(abs(int(replace_node[1])-1))

def change_fanin(network, netB, netA):
    for fin in netA[0].Fin:
        index = fin[0].Fout.index(netA[0])
        fin[0].Fout.remove(netA[0]) 


