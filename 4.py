'''
Find the least common ancestor between two nodes on a binary search tree.
The least common ancestor is the farthest node from the root that is an
ancestor of both nodes. For example, the root is a common ancestor of all
nodes on the tree, but if both nodes are descendents of the root's left child,
then that left child might be the lowest common ancestor. You can assume that
both nodes are in the tree, and the tree itself adheres to all BST properties.
The function definition should look like question4(T, r, n1, n2), where T
is the tree represented as a matrix, where the index of the list is equal
to the integer stored in that node and a 1 represents a child node, r is
a non-negative integer representing the root, and n1 and n2 are non-negative
integers representing the two nodes in no particular order. For example, one
test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

and the answer would be 3.
'''
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

# Function to return the immediate parent of a given node in the Tree T   
def get_parent(T, n):
    rows = len(T)
    for i in range(rows):
        # if the node value is 1 then, n is the child of i. So return i
        if T[i][n] == 1:
            return i
    # return -1 if no parent was found
    return -1


x = question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
# output is 3
print(x)
