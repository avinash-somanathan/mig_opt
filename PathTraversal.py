import parserNetwork 
import dataStructure
#from graphviz import Graph
import pdb

adjacency = dict()
temp_file_write = open("temp_file.txt",'w')

def create_adjacency(network):
    pi = list() 
    po = list() 
    for node in network.nodes.keys():
        edges = list()
        for i in range(0,len(network.nodes[node].Fout)):
                 edges.append(network.nodes[node].Fout[i].name)
        if network.nodes[node].nodeType == "Input":
            pi.append(network.nodes[node].name)
        if network.nodes[node].nodeType == "Output":
            po.append(network.nodes[node].name)
        adjacency[node] = edges
    print adjacency 
    return pi,po,adjacency

def find_all_paths(adjacency,destination):
    
  
    for source in adjacency.keys():
        visited = dict()
        for node in adjacency.keys():
            visited[node] = False
        path = []
        find_one_path(adjacency,source,destination,path,visited)

    temp_file_write.close()
    

def find_one_path(adjacency,source,destination,path,visited):

    update_value = {source : True}
    visited.update(update_value)
    path.append(source)
    
    if source in destination:
        print path
        temp_file_write.write(str(path) + "\n") 
         
    else :
        for node in adjacency[source]:
            if visited[node] == False:
                find_one_path(adjacency,node,destination,path,visited)
  
    path.pop()
    update_value = {source : False}
    visited.update(update_value)
    
def find_critical_paths(network):

    pi,po,adjacency = create_adjacency(network)
    #print adjacency
    mod_adjacency = dict()
    for node in adjacency.keys():
        #print list(set(pi)|set(po))
        if node not in pi:
                mod_adjacency[node] = adjacency[node]
    #draw_graph(adjacency)
    #print mod_adjacency
    find_all_paths(adjacency,po)

#def draw_graph(adjacency):
#    g = Graph('G',filename = 'Boolean_Network')
#    for node in adjacency:        
#        for Fout in adjacency[node]:
#            #print str(node) + " " + str(Fout)
#            g.edge(str(node),str(Fout))
#    g.view()
#        
parserNetwork.parser("networkOut.out")
find_critical_paths(parserNetwork.pNtk)
    
