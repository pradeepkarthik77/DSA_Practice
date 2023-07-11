class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left 
        self.right = right 

class BST:

    def __init__(self):
        self.root = None
    
    def insertNode(self,value):

        node = Node(value)

        if self.root is None:
            self.root = node 
            return 

        def insertUtil(node,root):
            if root is None:
                return node

            elif node.val < root.val:
                root.left = insertUtil(node,root.left)
            else:
                root.right = insertUtil(node,root.right)

            return root

        self.root = insertUtil(node,self.root)
    
    def inorder(self):

        arr = []

        def inorderUtil(root):
            if root is None:
                return 

            else:
                inorderUtil(root.left)
                arr.append(root.val)
                inorderUtil(root.right)


        inorderUtil(self.root)

        return arr

    def preorder(self):

        arr = []

        def preorderUtil(root):
            if root is None:
                return 

            else:
                arr.append(root.val)
                preorderUtil(root.left)
                preorderUtil(root.right)


        preorderUtil(self.root)

        return arr

    def postorder(self):

        arr = []

        def postorderUtil(root):
            if root is None:
                return 

            else:
                postorderUtil(root.left)
                postorderUtil(root.right)
                arr.append(root.val)


        postorderUtil(self.root)

        return arr

if __name__=="__main__":
    bst = BST()
    bst.insertNode(5)
    bst.insertNode(4)
    bst.insertNode(6)
    bst.insertNode(1)
    bst.insertNode(2)
    print(bst.inorder())
    print(bst.preorder())
    print(bst.postorder())
    
    
    
