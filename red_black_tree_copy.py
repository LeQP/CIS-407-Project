class Student(object):
    def __init__(self, name):
        self.name
        self.crn = []
        self.classes = []
        self.attended = 0

    # Setters
    def set_name(self, new_name):
        self.name = new_name
    def add_crn(self, crn):
        self.crn.append(crn)
    def remove_crn(self, crn):
        self.crn.remove(crn)
    def add_classes(self, classes):
        self.classes.append(classes)
    def remove_classes(self, classes):
        self.classes.remove(classes)
    def add_attended(self):
        self.attended = self.attended + 1
    def subtract_attended(self):
        self.attended = self.attended - 1

    # Getters
    def print_all(self):
        print(f"Name: {self.name}\nCRNs: {self.crn}\nClasses: {self.classes}\nAttended: {self.attended}")
        
class Node(object):
    def __init__(self, id, name, left = None, right = None, parent = None, color = 'red'):
        # Student Information
        self.id = id
        self.student = Student(name)
        
        # Tree Properties
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class rb_tree(object):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    # initialize root and size
    def __init__(self):
        self.root = None
        self.sentinel = Node(None, None, None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel

    def print_specific(self, id  = 0, name = ""):
       print("==============================")
       self.__print_specific(self.root, id, name)

        
    def __print_specific(self, curr_node, id, name):
       if curr_node is not self.sentinel:
            self.__print_specific(curr_node.left, id, name)
            if (curr_node.id == id) or (curr_node.student.name == name):
               print("External Student ID: " + str(curr_node.id))
               curr_node.student.print_all()
               print("==============================")
            self.__print_specific(curr_node.right, id, name)

    # Name is cryptic hash name
    def find_name(self, name):
        if self.root:
            result = self.__find_name(name, self.root)
            if result != None:
                return result
            else:
                return None
        else:
            raise KeyError("KeyError detected: Tree has no root")

    def __find_name(self, name, curr_node):
        if curr_node is self.sentinel:
            return None
        elif (curr_node.student.name == name):
            return curr_node
        else:
            result1 = self.__find_name(name, curr_node.left)
            result2 = self.__find_name(name, curr_node.right)
            if result1 != None:
                return result1
            elif result2 != None:
                return result2
            else:
                return None

    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False
    
    def print_tree(self):
        # Print the IDs of all nodes in order
        print("==============================")
        self.__print_tree(self.root)
    
    def __print_tree(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in inorder
        if curr_node is not self.sentinel:
            self.__print_tree(curr_node.left)
            print("External Student ID: " + str(curr_node.id))
            curr_node.student.print_all()
            print("==============================")
            self.__print_tree(curr_node.right)
    
    def print_with_colors(self):
        # Also prints the IDs of all node but with color indicators
        self.__print_with_colors(self.root)

    def __print_with_colors(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in INORDER
        # Extracts the color of the node and print it in the format -idC- where C is B for black and R for red
        if curr_node is not self.sentinel:
            if curr_node.color == "red":
                node_color = "R"
            else:
                node_color = "B"
            
            self.__print_with_colors(curr_node.left)
            print("External Student ID: " + str(curr_node.id))
            curr_node.student.print_all()
            self.__print_with_colors(curr_node.right)

                   
    def __iter__(self):
        return self.inorder()
    def inorder(self):
        return self.__traverse(self.root, rb_tree.INORDER)
    def preorder(self):
        return self.__traverse(self.root, rb_tree.PREORDER)
    def postorder(self):
        return self.__traverse(self.root, rb_tree.POSTORDER)
    def __traverse(self, curr_node, traversal_type):
        if curr_node is not self.sentinel:
            if traversal_type == self.PREORDER:
                yield curr_node
            yield from self.__traverse(curr_node.left, traversal_type)
            if traversal_type == self.INORDER:
                yield curr_node
            yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == self.POSTORDER:
                yield curr_node
    
    # find_node expects a ID and returns the Node object for the given ID
    def find_node(self, id):
        if self.root:
            desired_id = self.__get(id, self.root)
            if desired_id:
                return desired_id
            else:
                return None
        else:
            raise KeyError("KeyError detected: Tree has no root")

    # helper function __get receives a data and a node. Returns the node with
    # the given ID
    def __get(self, id, current_node):
        if current_node is self.sentinel: # if current_node does not exist return None
            return None
        elif current_node.id == id:
            return current_node
        elif id < current_node.id:
            # recursively call __get with ID and current_node's left
            return self.__get( id, current_node.left )
        else: # ID is greater than current_node.ID
            # recursively call __get with ID and current_node's right
            return self.__get( id, current_node.right )

    def find_successor(self, id):
        # Private Method, can only be used inside of BST.
        current_node = self.find_node(id)
        if current_node is self.sentinel:
            raise KeyError
        # Travel left down the rightmost subtree
        if current_node.right:
            current_node = current_node.right
            while current_node.left is not self.sentinel:
                current_node = current_node.left
            successor = current_node
        # Travel up until the node is a left child
        else:
            parent = current_node.parent
            while parent is not self.sentinel and current_node is not parent.left:
                current_node = parent
                parent = parent.parent
            successor = parent
        if successor:
            return successor
        else:
            return None

    # Adds a node to the tree
    def insert(self, id, name = ""):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            new_node = self.__put(id, name, self.root)
            self.__rb_insert_fixup(new_node)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(id, name, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)
        
    # helper function __put finds the appropriate place to add a node in the tree
    def __put(self, id, name, current_node):
        if id < current_node.id:
            if current_node.left != self.sentinel:
                new_node = self.__put(id, name, current_node.left)
            else: # current_node has no child
                new_node = Node(id, name, parent = current_node, left = self.sentinel, right = self.sentinel )
                current_node.left = new_node
        else: # ID is greater than or equal to current_node's ID
            if current_node.right != self.sentinel:
                new_node = self.__put(id, name, current_node.right)
            else: # current_node has no right child
                new_node = Node(id, name, parent = current_node,left = self.sentinel,right = self.sentinel )
                current_node.right = new_node
        return new_node

    def delete(self, id):
        # Same as binary tree delete, except we call rb_delete fixup at the end.
        z = self.find_node(id)
        if z.left is self.sentinel or z.right is self.sentinel:
            y = z
        else:
            y = self.find_successor(z.id)
        if y.left is not self.sentinel:
            x = y.left
        else:
            x = y.right
        if x is not self.sentinel:
            x.parent = y.parent
        if y.parent is self.sentinel:
            self.root = x
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        if y is not z:
            z.id = y.id
        if y.color == 'black':
            if x is self.sentinel:
                self.__rb_delete_fixup(y)
            else:
                self.__rb_delete_fixup(x)

    def left_rotate(self, current_node):
        """
        Peforms a left rotation on a node and its right child

        Parameters:
        -----------
        current_node : Node
            The root node of a subtree that will be rotated alongside its right child

        Raises:
        -------
        KeyError
            Occurs by trying to rotate a NULL or sentinel node

        """

        x = current_node                # Define x as the root of the subtree
        try:                            # Check for current node and if tree is empty to see if rotation is possible
            if self.root == self.sentinel or self.root == None or x == self.sentinel or x == None:  
                raise KeyError
        except KeyError:
            print("KeyError detected: Can't do a left rotation with node or its right child")
            raise KeyError

        y = x.right                     # Define y as the right child to rotate with x
        try:                            # Check for node and child to see if rotation is possible
            if y == self.sentinel or y == None:  
                raise KeyError
        except KeyError:
            print("KeyError detected: Can't do a left rotation with node or its right child")
            raise KeyError

        x.right = y.left                # Set y's left subtree as x's right subtree
        if y.left != self.sentinel:     # Adjust parent if the left subtree is not NULL
            y.left.parent = x

        y.parent = x.parent             # Take x out between x's parent and y by setting y's new parent as x's parent
        if x.parent == self.sentinel:   # Make y the root if x happens to be the root
            self.root = y               
        elif x == x.parent.left:        # Make y the new left child if x was a left child   
            x.parent.left = y           
        else:                           # Make y the new right child if x was a right child
            x.parent.right = y

        y.left = x;                     # Complete the swap and adjustments between x and y by making x the left child of y and y as the parent
        x.parent = y
    
    def right_rotate(self, current_node):
        """
        Peforms a right rotation on a node and its left child

        Parameters:
        -----------
        current_node : Node
            The root node of a subtree that will be rotated alongside its left child

        Raises:
        -------
        KeyError
            Occurs by trying to rotate along with a NULL or sentinel

        """
        y = current_node                # Define y as the root of the subtree
        try:                            # Check for current node and if tree is empty to see if rotation is possible
            if self.root == self.sentinel or self.root == None or y == self.sentinel or y == None:  
                raise KeyError
        except KeyError:
            print("KeyError detected: Can't do a right rotation with node or its left child")
            raise KeyError

        x = y.left                      # Define x as the left child to rotate with y
        try:                            # Check for x's left child to see if rotation is possible
            if x == self.sentinel or x == None:  
                raise KeyError
        except KeyError:
            print("KeyError detected: Can't do a right rotation with node or its left child")
            raise KeyError

        y.left = x.right                # Set x's right subtree as y's left subtree
        if x.right != self.sentinel:    # Adjust parent if the right subtree is not NULL
            x.right.parent = y

        x.parent = y.parent             # Take y out between y's parent and x by setting x's new parent as y's parent
        if y.parent == self.sentinel:   # Make x the root if y happens to be the root
            self.root = x
        elif y == y.parent.left:        # Make x the new left child if y was a left child 
            y.parent.left = x
        else:                           # Make x the new right child if y was a right child
            y.parent.right = x

        x.right = y;                    # Complete the rotation and adjustments between y and x by making y the right child of x and x as the parent
        y.parent = x
    
    def __rb_insert_fixup(self, z):
        """
        Helper function maintains the balancing and coloring property after insertion into a red-black tree

        Parameters:
        -----------
        z : Node
            A value to reference a specific node and its parent; starts at the newly inserted node and later moves up the tree,
        
        Raises:
        -------
        KeyError
            Occurs by trying to rotate along with a NULL or sentinel child using left_rotate() or right_rotate()
        """
        
        # Use a while-loop to keep moving up the tree to check for consecutive reds and stop once reds are no longer consecutive
        # z is assumed red, so check for the parent's color
        while z.parent.color == "red":
            # Create two different cases to determine z's "uncle" y or the sibling of z's parent
            # Each case has 2 subcases that deal with y being black or red
            if z.parent == z.parent.parent.left:    # Case 1: y is a right child
                y = z.parent.parent.right           
                if y.color == "red":                # Case A: y is red, so do a color shift and move z up to check other nodes
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                elif y.color == "black":            # Case B: y is black, so do rotation and should fix the consecutive red issue
                    if z == z.parent.right:         # Subcase of B where z is a right child, so a double rotation needs to occur
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            else:                                   # Case 2: y is a left child
                y = z.parent.parent.left            
                if y.color == "red":                # Case A: y is red, so do a color shift and move z up to check other nodes
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                elif y.color == "black":            # Case B: y is black, so do rotation and should fix the consecutive red issue
                    if z == z.parent.left:          # Subcase of B where z is a left child, so a double rotation needs to occur
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "black"                   # Manually make the root black to maintain black root color at the end of the fixup


    def __rb_delete_fixup(self, x):
        """ 
        Helper function that maintains the balancing and coloring property after bst deletion 

        Parameters:
        -----------
        x : Node
            x initially represents the node once that gets deleted

        Raises:
        -------
        KeyError
            Occurs by trying to rotate along with a NULL or sentinel child using left_rotate() or right_rotate()
        """
        # Use a while-loop to check if x is a red, since that can be easily done by changing red to black, and if there are still elements in the tree after deletion
        # Iterate through loop until x is red
        while x != self.root and x.color == "black":
            # Create two cases to  check if x is a left or right child.
            # Each case has four subcases that consider w and its children
            # w is consistently x's sibling

            if x == x.parent.left:  # Case 1: x is a left child
                w = x.parent.right

                # Case A: w is red, so left rotate w and its parent and swap their colors
                if w.color == "red":                                                              
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)

                    w = x.parent.right # Adjust w to maintain its status as x's sibling after rotation
                # Case B: w and both its children are black
                # so set w to red and relocate x to its parent
                elif w.color == "black" and w.left.color == "black" and w.right.color == "black": 
                    w.color = "red" 
                    x = x.parent

                # Case C: w and its right child are black and w's left child is red
                # so switch w and its left child's color and right rotate both of them
                elif w.color == "black" and w.left.color == "red" and w.right.color == "black":   
                    w.left.color = "black"                                                        
                    w.color = "red"
                    self.right_rotate(w)
                    w = x.parent.right  # Adjust w to maintain its status as x's sibling after rotation

                # Case D: w is black and its right child is red
                # so swtich colors between w and it parent, set w' right child's color to black, and do a left rotation on x's parent and w
                elif w.color == "black" and w.right.color == "red":                               
                    w.color = x.parent.color                         
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root # Set x as the root finish the deletion process

            else: # Case 2: x is a right child
                w = x.parent.left

                # Case A: w is red, so right rotate w and its parent and swap their colors
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left # Adjust w to maintain its status as x's sibling after rotation

                # Case B: w and both its children are black
                # so set w to red and relocate x to its parent
                elif w.color == "black" and w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent

                # Case C: w and its left child are black and w's right child is red
                # so switch w and its right child's color and left rotate both of them
                elif w.color == "black" and w.right.color == "red" and w.left.color == "black":
                    w.right.color = "black"
                    w.color = "red"
                    self.left_rotate(w)
                    w = x.parent.left # Adjust w to maintain its status as x's sibling after rotation
                    
                # Case D: w is black and its left child is red
                # so switch colors between w and its parent, set w' left child's color to black, and do a right rotation on x's parent and w
                elif w.color == "black" and w.left.color == "red":
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root # Set x as the root finish the deletion process
        x.color = "black" # Set x to black at the end of the method
                    
