#from binarytree import tree, bst, heap
class tree:
    def __init__(self,val = None):
        self.val = val
        self.left = None
        self.right = None
    """def display_root(self):
        temp = None
        while self != None"""
s = 0


def calculatemaxpath(root: tree): #FROOM ROOT
    if root == None:
        return 0
    left  = calculatemaxpath(root.left)
    right = calculatemaxpath(root.right)
    return max(left,right) + root.val

#sum = 0
def maxpath(root: tree): #from every root
    g = []
    sum = 0
    helper(root, sum, g)
    #sum = helper(root, sum, g)
    #return sum
    return(max(g))
    #return sum
def helper(root: tree, sum, g):
    if root == None:
        return sum
    left = max(helper(root.left,sum, g), 0)
    right = max(helper(root.right,sum, g), 0)
    sum = max(sum, max(left, right) + root.val)
    g.append(sum)
    return max(left, right) + root.val

if __name__ == "__main__":
    """root = tree(1)
    root.left = tree(2)
    root.right = tree(3)
    root.left.left = tree(4)
    root.left.right = tree(6)
    root.left.left.left = tree(10)"""
    g = 0
    root = tree(-10)
    root.left = tree(9)
    root.right = tree(20)
    root.right.right = tree(8)
    root.right.right.right = tree(-2)

    root.right.left = tree(-3)
    root.right.left.left = tree(5)
    root.right.left.left.left = tree(-2)
    root.right.left.right = tree(-4)

    print(maxpath(root))
    print(calculatemaxpath(root))
    #print(sum)
    #maxpath(g,root)
    #print(g)
