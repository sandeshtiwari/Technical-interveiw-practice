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
    print(temp_dict)

    for i in a1:
        for j in a1[i]:
            print (temp_dict[i], temp_dict[j[0]], j[1])
            u,v,w = temp_dict[i], temp_dict[j[0]], j[1]
            graph.append([u,v,w])
    print (graph)

    return 1



al = {'A': [('B', 2)],
        'B': [('A', 4), ('C', 2)],
        'C': [('A', 2), ('B', 5)]}
print (question3(al))


