# Funciton to return the lowest common parent of two nodes in a tree
def question4(T, r, n1, n2):
    # list to store all the ancestors of  the node n1
    parents_of_n1 = []
    # Finding and storing all the ancestors of node n1 till we find the root
    while n1 != r:
        # getting the parent node of n1 and storing in n1
        n1 = get_parent(T, n1)
        parents_of_n1.append(n1)
    # if no ancestors were there, return -1
    if len(parents_of_n1) == 0:
        return -1
    # Looping until n2 is root
    while n2 != r:
        n2 = get_parent(T, n2)
        # if a ancestor of n2 is a ancestor of n1, then return the particular ancestor
        if n2 in parents_of_n1:
            return n2
    return -1
