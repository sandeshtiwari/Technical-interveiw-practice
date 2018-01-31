def question3(a1):
    n = len(a1)
    temp_dict = {}
    reversed_dict = {}
    count = 0
    u,v,w = None, None, None
    graph = []
    for i in a1:
        temp_dict[i] = count
        #print(temp_dict)
        reversed_dict[count] = i
        #print(reversed_dict)
        count += 1
    #print(temp_dict)

    for i in a1:
        for j in a1[i]:
            #print (temp_dict[i], temp_dict[j[0]], j[1])
            u,v,w = temp_dict[i], temp_dict[j[0]], j[1]
            graph.append([u,v,w])
    #print (graph)

    return KruskalMST(graph, count, reversed_dict)

# The main function to build MST using Kruskal's algorithm
def KruskalMST(graph, V, reversed_dict):

    result =[] #This will store the resultant MST

    i = 0 # An index variable, used for sorted edges
    e = 0 # An index variable, used for result[]

    #Step 1:  Sort all the edges in non-decreasing order of their
    # weight.  If we are not allowed to change the given graph, we
    # can create a copy of graph
    graph =  sorted(graph,key=lambda item: item[2])

    parent = [] ; rank = []

    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < V -1 :

        # Step 2: Pick the smallest edge and increment the index
        # for next iteration
        u,v,w =  graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent ,v)

        # If including this edge does't cause cycle, include it
        # in result and increment the index of result for next edge
        if x != y:
            e = e + 1
            result.append([u,v,w])
            union(parent, rank, x, y)
        # Else discard the edge

    # print the contents of result[] to display the built MST
    #print "Following are the edges in the constructed MST"
    p1 = []
    final_result = {}
    for u,v,weight  in result:
        p1 = [(reversed_dict[v],weight)]
        if reversed_dict[u] not in final_result:
            final_result[reversed_dict[u]] = p1
        else:
            final_result[inv_dict[u]] = final_result[reversed_dict[u]].append(p1)
    return final_result

# A utility function to find set of an element i
# (uses path compression technique)
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# A function that does union of two sets of x and y
# (uses union by rank)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of high rank tree
    # (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    #If ranks are same, then make one as root and increment
    # its rank by one
    else :
        parent[yroot] = xroot
    rank[xroot] += 1

al = {'A': [('B', 2)],
        'B': [('A', 4), ('C', 2)],
        'C': [('A', 2), ('B', 5)]}
print (question3(al))


