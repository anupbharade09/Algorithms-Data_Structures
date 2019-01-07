outputdebug = False

def debug(msg):
    if outputdebug:
        print(msg)

# a class to create a node
class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Class for for AVL tree implementation
class AVLTree():
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0;

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    # height function
    def height(self):
        if self.node:
            #print(self.node.height)
            return self.node.height
        else:
            return 0

    # function to check if there leaf
    def is_leaf(self):
        return (self.height == 0)

    # Insertion function to add new node to BST
    def insert(self, key):
        tree = self.node
        newnode = Node(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        else:
            debug("Key [" + str(key) + "] already in tree.")

        self.rebalance()

    # function for re-balancing BST after insertion of new node
    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.key) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.key) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None:
            if self.node.key == key:
                debug("Deleting ... " + str(key))
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None  # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None:  # sanity check
                        debug("Found replacement for " + str(key) + " -> " + str(replacement.key))
                        self.node.key = replacement.key

                        # replaced. Now delete the key from right child
                        self.node.right.delete(replacement.key)

                self.rebalance()
                return
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        '''
        Find the biggest valued node in LEFT child
        '''
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        '''
        Find the smallese valued node in RIGHT child
        '''
        node = node.right.node
        if node != None:  # just a sanity check

            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            print('True')
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def is_max_heap(self):
        '''(BTNode) -> bool

        Return True iff the binary tree rooted at node is a max-heap
        Precondition: the tree is complete.

        '''
        #if not (self.node.left or self.node.right):
        if  (self.node.left.node == None and self.node.right.node == None):
            return True

        if self.node.right.node == None:
            return True
        if self.node.left.node == None:
            return True
        else:
            if self.node.key > self.node.left.node.key and self.node.key > self.node.right.node.key:
                return self.node.left.is_max_heap() and self.node.right.is_max_heap()
            else:
                return False

    # displaying elements in inorder traversal
    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    # code to check anagrams in give tree
    def chk_anagrams(self,l):
        anagrams = {}
        for i in l:
            anagrams[i] = 0
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i] != l[j]:
                    if sorted(l[i]) == sorted(l[j]):
                        anagrams[l[i]] = anagrams[l[i]] + 1

        print('Anagram Count: ')
        for i in anagrams:
            print(i, '-', anagrams[i])

# Usage example
if __name__ == "__main__":
    a = AVLTree()

    print('Welcome to this program')
    print('You may use following operations to create Balanced Binary Search Tree: ')
    print('1. Create \n 2. Height \n 3. Insert \n 4. Delete \n 5. Display \n 6. Check max heap \n 7. Anagrams \n 8. Exit')

    while True:

        choice = input(('Enter number for above operations: '))
        if choice == '1':
            print('Please provide elements and number of elements for creation of BST. Press enter after every input')
            inlist = []
            maxLengthList = int(input('Total number of elements: '))
            while len(inlist) < maxLengthList:
                item = input("Enter element: ")
                inlist.append(item)
        #inlist = ['king', 'ingk', 'rook', 'Bishop', 'pawn','wnap']
            for i in inlist:
                a.insert(i)
        elif choice == '2':
            h = a.height
            print('Height of the tree is: ',h)
        elif choice == '3':
            i = input('Type element which needs to be inserted: ')
            a.insert(i)
            print('Element is inserted. You may use display function')
        elif choice == '4':
            elm_choice = input("Which element you want to delete ? ")
            a.delete(elm_choice)
            print('Element deleted. You may use display function.')
        elif choice == '5':
            print("Inorder traversal:", a.inorder_traverse())
        elif choice == '6':
            if (a.is_max_heap()):
                print('Yes it is max heap')
            else:
                print('Not a max heap')
        elif choice == '7':
            l = a.inorder_traverse()
            a.chk_anagrams(l)
        elif choice == '8':
            break