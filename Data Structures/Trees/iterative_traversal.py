class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left 
        self.right = right 

class BST:

    def __init__(self):
        self.root = None
    
    def insertNode(self,value):

        curr = self.root 

        node = Node(value)

        if self.root is None:
            self.root = node
            return

        while curr:
            if node.val < curr.val:
                if curr.left is None:
                    curr.left = node
                    break
                else:
                    curr = curr.left 
            else:
                if curr.right is None:
                    curr.right = node 
                    break
                else:
                    curr = curr.right
    
    def inorder(self):

        stack = []
        arr = []

        curr = self.root 

        while True:

            if curr is not None:
                stack.append(curr)
                curr = curr.left 
            
            elif len(stack)!=0:
                curr = stack.pop(-1)
                arr.append(curr.val)
                print(arr[-1],end=" ")
                curr = curr.right
            
            else:
                print("hi")
                break
        
        return arr

    def preorder(self):

        arr = []

        curr = self.root 
        stack = []

        while True:

            if curr is not None:
                arr.append(curr.val)
                stack.append(curr)
                curr = curr.left
            
            elif stack:
                curr = stack.pop(-1)
                curr = curr.right
            
            else:
                break

        return arr

    def postorder(self):

        arr = []

        curr = self.root
        stack = []

        while True:
            if curr is not None:
                arr.append(curr.val)
                stack.append(curr)
                curr = curr.right 
            
            elif stack:
                curr = stack.pop(-1)
                curr = curr.left
            else:
                break

        return arr[::-1]

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
    
    
    
