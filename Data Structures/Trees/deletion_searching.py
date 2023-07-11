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

    def levelorder(self):

        curr = self.root 

        if curr is None:
            return []

        currarr = [self.root]
        nextarr = []
        arr = []

        while currarr:

            element = currarr.pop(0)
            arr.append(element.val)

            if element.left is not None:
                nextarr.append(element.left)
            if element.right is not None:
                nextarr.append(element.right)

            if currarr == []:
                currarr = nextarr.copy()
                nextarr = []
        
        return arr

    def recurse_search(self,element):
        
        def R_Search(node,element):

            if node is None:
                return False
            
            elif node.val == element:
                return True

            elif node.val > element:
                return R_Search(node.left,element)
            else:
                return R_Search(node.right,element)
        
        return R_Search(self.root,element)

    def iterative_search(self,element):
        
        curr = self.root 

        while curr:

            if curr.val == element:
                return True 

            elif curr.val > element:
                curr = curr.left 
            
            else:
                curr = curr.right 
        
        else:
            return False
    
    def deleteNode(self,root, X):
    # code here.
    
        if root is None:
            return root
        
        elif root.val == X:
            
            if root.left is None and root.right is None:
                return None
            
            elif root.left is None or root.right is None:
                
                if root.left is not None:
                    root.val,root.left.val = root.left.val,root.val
                    root.left = self.deleteNode(root.left,X)
                
                else:
                    root.val,root.right.val = root.right.val,root.val
                    root.right = self.deleteNode(root.right,X)
                
            else:
                
                temp = root.right
                
                while temp.left:
                    temp = temp.left
                
                root.val,temp.val = temp.val,root.val
                root.right = self.deleteNode(root.right,X)
                
        else:
            root.right = self.deleteNode(root.right,X)
            root.left = self.deleteNode(root.left,X)
        
        return root

    def deleteIt(self,item):

        self.root = self.deleteNode(self.root,item)
     

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
    print(bst.levelorder())
    print(bst.recurse_search(1))
    print(bst.iterative_search(100))
    bst.deleteIt(5)
    print(bst.inorder())
    
    
