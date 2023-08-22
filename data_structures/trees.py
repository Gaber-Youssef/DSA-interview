"""
* Quick summary: 
    - a data structure that stores a hierarchy of values.
* Important facts:
    - Organizes values hierarchically.
    - A tree item is called a node, and every node is connected to 0 or more child nodes using links.
    - A tree is a kind of graph where between any two nodes, there is only one possible path.
    - The top node in a tree that has no parent nodes is called the root.
    - Nodes that have no children are called leaves.
    - The number of links from the root to a node is called that node's depth.
    - The height of a tree is the number of links from its root to the furthest leaf.
    - In a binary tree, nodes cannot have more than two children.
        - Any node can have one left and one right child node.
        - Used to make binary search trees.
        - In an unbalanced binary tree, there is a significant difference in height between subtrees.
        - An completely one-sided tree is called a degenerate tree and becomes equivalent to a linked list.
    - Trees (and graphs in general) can be traversed in several ways:
        - Breadth first search (BFS): nodes one link away from the root are visited first, then nodes two links away, etc. BFS finds the shortest path between the starting node and any other reachable node.
        - Depth first search (DFS): nodes are visited as deep as possible down the leftmost path, then by the next path to the right, etc. This method is less memory intensive than BFS. It comes in several flavors, including:
            - Pre order traversal (similar to DFS): after the current node, the left subtree is visited, then the right subtree.
            - In order traversal: the left subtree is visited first, then the current node, then the right subtree.
            - Post order traversal. the left subtree is visited first, then the right subtree, and finally the current node.
* Pros:
    - For most operations, the average time complexity is O(log(n)), which enables solid scalability. Worst time complexity varies between O(log(n)) and O(n).
* Cons:
    - Performance degrades as trees lose balance, and re-balancing requires effort.
    - No constant time operations: trees are moderately fast at everything they do.
* Notable uses:
    - File systems.
    - Database indexing.
    - Syntax trees.
    - Comment threads.
* Time complexity: 
    - varies for different kinds of trees.

* ################################################
* ############## Binary Search Tree ##############
* ################################################

* Quick summary: 
    - a kind of binary tree where nodes to the left are smaller, and nodes to the right are larger than the current node.
* Important facts:
    - Nodes of a binary search tree (BST) are ordered in a specific way:
        - All nodes to the left of the current node are smaller (or sometimes smaller or equal) than the current node.
        - All nodes to the right of the current node are larger than the current node.
    Duplicate nodes are usually not allowed.
* Pros:
    - Balanced BSTs are moderately performant for all operations.
    - Since BST is sorted, reading its nodes in sorted order can be done in O(n), and search for a node closest to a value can be done in O(log(n))
* Cons:
    Same as trees in general: no constant time operations, performance degradation in unbalanced trees.
* Time complexity (worst case):
    Access: O(n)
    Search: O(n)
    Insertion: O(n)
    Deletion: O(n)
* Time complexity (average case):
    Access: O(log(n))
    Search: O(log(n))
    Insertion: O(log(n))
    Deletion: O(log(n))
    
"""
from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
        
    def printTree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preOrderTraversal(self.root, "")
        elif traversal_type == "inorder":
            return self.inOrderTraversal(self.root, "")
        elif traversal_type == "postorder":
            return self.postOrderTraversal(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelOrderTraversal(self.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False
        
    def preOrderTraversal(self, start, traversal):
        """
        Pre-order traversal visits the current node first, then the left subtree, and finally the right subtree.
        """
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preOrderTraversal(start.left, traversal)
            traversal = self.preOrderTraversal(start.right, traversal)
        return traversal
    
    def inOrderTraversal(self, start, traversal):
        """
        In-order traversal visits the left subtree first, then the current node, and finally the right subtree.
        """
        if start:
            traversal = self.inOrderTraversal(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inOrderTraversal(start.right, traversal)
        return traversal
    
    def postOrderTraversal(self, start, traversal):
        """
        Post-order traversal visits the left subtree first, then the right subtree, and finally the current node.
        """
        if start:
            traversal = self.postOrderTraversal(start.left, traversal)
            traversal = self.postOrderTraversal(start.right, traversal)
            traversal += (str(start.data) + "-")
        return traversal
    
    def levelOrderTraversal(self, start):
        """
        Level-order traversal visits each level of the tree from left to right.
        """
        if start is None:
            return
        queue = Queue()
        queue.put(start)
        traversal = ""
        while not queue.empty():
            node = queue.get()
            traversal += str(node.data) + "-"
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
        return traversal
    
    def insert(self, data, current_node):
        """
        Insertion adds a new node to the tree.
        """
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self.insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self.insert(data, current_node.right)
        else:
            print("Value is already present in tree.")
            
    def getMinValue(self, current_node):
        """
        Returns the minimum value found in the tree.
        """
        if current_node.left is None:
            return current_node.data
        else:
            return self.getMinValue(current_node.left)
        
    def getMaxValue(self, current_node):
        """
        Returns the maximum value found in the tree.
        """
        if current_node.right is None:
            return current_node.data
        else:
            return self.getMaxValue(current_node.right)
        
    def search(self, data):
        """
        Searches the tree for a node with the given data.
        """
        if self.root:
            isFound = self._searchHelper(data, self.root)
            if isFound:
                return True
            return False
        else:
            return None
        
    def _searchHelper(self, data, current_node):
        """
        The function is a helper function for searching for a specific value in a binary search tree.
        
        :param data: The value we are searching for in the binary search tree
        :param current_node: The current_node parameter represents the current node being checked during
        the search process in a binary search tree. It is used to traverse the tree and compare the data
        value with the current node's data value
        :return: a boolean value. If the data is found in the current node, it returns True. If the data
        is less than the current node's data and there is a left child node, it recursively calls the
        function on the left child node. If the data is greater than the current node's data and there
        is a right child node, it recursively calls the function on the right child
        """
        if data == current_node.data:
            return True
        elif data < current_node.data and current_node.left:
            return self._searchHelper(data, current_node.left)
        elif data > current_node.data and current_node.right:
            return self._searchHelper(data, current_node.right)
        
    
        
if __name__ == "__main__":
    # test binary tree
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    
    print(tree.printTree("preorder"))
    print(tree.printTree("inorder"))
    print(tree.printTree("postorder"))
    print(tree.printTree("levelorder"))
    
    tree.insert(6, tree.root)
    print(tree.printTree("levelorder"))
    
    print(tree.getMinValue(tree.root))
    print(tree.getMaxValue(tree.root))
    
    print(tree.search(4))
    print(tree.search(6))
    print(tree.search(7))
        