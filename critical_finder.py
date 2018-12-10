import dataStructure 
import parserNetwork
import PathTraversal
import operator 
import pdb
node_criticality = dict()

def Sort_Levels(network):
    
    Sorted_Level_List = dict()
    pdb.set_trace()
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
    pdb.set_trace()
    for level in reversed(Sorted_Level_List.keys()):
        for node in range(len(Sorted_Level_List[level])):
            temp_node = Sorted_Level_List[level][node]
            criticality_fout = 0
            for node in temp_node.Fout:
                criticality_fout += node_criticality[node.name]
            criticality = float(len(temp_node.Fout))*(0.33333) + float(criticality_fout)*(0.33333)
            node_criticality[temp_node.name] = criticality
            print "Level : %d  Node Name : %d Criticality : %.5f "%(temp_node.level,temp_node.name,criticality)
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

    print critical_voters_list
    pdb.set_trace()
    return critical_voters_list




def introduce_error(critical_voters_list,network):

    #Case A : critical_voter[0] = critical_voter[1]_bar     

    
    newNtk = dataStructure.network.copy(network)

    a = dataStructure.network.getNode(network,critical_voters_list[0])
    b = dataStructure.network.getNode(network,critical_voters_list[1])
    if a.level < b.level :
        temp = a
        a = b
        b = temp
    complement = '0'
    
    change_fanout(network,correct_node,error_node,complement)
    change_fanin(network,correct_node,error_node,complement)

def change_fanout(network,correct_node,error_node,complement):
    for fout in correct_node.Fout:
        for replace_node in fout.Fin:
            if replace_node[0].name == correct_node.name:
                #print "Previous Fanin of  " + str(fout.name) + " is " + str(replace_node[0].name)
                replace_node[0] = error_node
                replace_node[1] = complement
                #print "New Fanin of " + str(fout.name) + " is " + str(replace_node[0].name)
            
#def change_fanin(network,correct_node,error_node,complement):
#    for fin in correct_node.Fin:
        #print fin
    
#parserNetwork.parser("networkOut.out")
#find_connected_nodes(parserNetwork.pNtk)
#print node_criticality

