"""
red_black_tree: A program that contains the red-black tree data structure to store nodes
based on two colors: red and black. This is based on code Joey Le has worked on for CIS 313 
and has been modified to the context of collect_student_info.

Rationale: Each student contains a significant amount of information needed to be stored. While
it is possible to contain all that information in a list and store that list in a list full of lists,
a red_black_tree allows a more simplier representation of the information that gets stored by using nodes.
Another advantage is that searching for a node based on a student's 95-number through find_node() can
allow a O(log n) search, faster than doing a O(n) search for a list containing student information under one item. 

"""


# Student: a class used as a storage unit for a student's information: first name, last name, 
# CRNs, class names, and amount of Class Encore sessions attended.
class Student(object):
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
        self.crn = []
        self.classes = []
        self.attended = 0

    # Setters - alter a specic attribute if needed
    def set_first(self, first_name):
        self.first = first_name
    def set_last(self, last_name):
        self.last = last_name
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

    # Getters - retrieve or print student infromation
    def get_full_name(self):
        full_name = str(self.first) + " " + str(self.last)
        return full_name
    def print_all(self):
        full = self.get_full_name()
        print(f"Name: {full}\nCRNs: {self.crn}\nClasses: {self.classes}\nAttended: {self.attended}")

# Node: a class used to store in the red-black tree and is identifiable by a student's 95-number
# Input: a student's first name and a student's last name
class Node(object):
    def __init__(self, id, first = "", last = "", left = None, right = None, parent = None, color = 'red'):
        # Student Information
        self.id = id
        self.student = Student(first, last)
        
        # Tree Properties
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

# rb_tree: a class that represents the red-black tree data structure
class rb_tree(object):
    # Attributes for a specific print order
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    # Initialize root and sentinel
    def __init__(self):
        self.root = None
        self.sentinel = Node(None, None, None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel

    # Print a specific student's information
    # Input: a student's 95-number or their first and last name but not both 95-number and name
    # Errors: KeyError - when attempting to print from an empty tree
    def print_specific(self, id  = 0, first  = "", last = ""):
        # Check if the tree is empty first
        if self.is_empty() == False:
            print("==============================")
            self.__print_specific(self.root, id, first, last)
        else:
            raise KeyError("KeyError detected: Tree has no information stored")

    # Helper function for print_specific; uses recursion to iterate through the whole tree through inorder traversal
    # Input: the tree's root to start, and a student's 95-number or their first and last name but not both 95-number and name
    def __print_specific(self, curr_node, id, first, last):
       if curr_node is not self.sentinel:
            self.__print_specific(curr_node.left, id, first, last)
            # Check a node's student information to determine if it should print
            if (curr_node.id == id and first == "" and last == "") or (id == 0 and curr_node.student.first == first and curr_node.student.last == last):
               print("External Student ID: " + str(curr_node.id))
               curr_node.student.print_all()
               print("==============================")
            self.__print_specific(curr_node.right, id, first, last)


    # Returns a node containing a specific student's information by searching based on a name
    # Input: a student's first and last name
    # Errors: KeyError - when attempting to find a name for an empty tree
    def find_name(self, first, last):
        if self.root:
            result = self.__find_name(first, last, self.root)
            if result != None:
                return result
            else:
                return None
        else:
            raise KeyError("KeyError detected: Tree has no root")

    # Helper function for find_name
    # Input: a student's first and last name and the tree's root in order to start
    def __find_name(self, first, last, curr_node):
        # When the leaves are reached, return None
        if curr_node is self.sentinel:
            return None
        # When the node with the desired name is found, return the node
        elif (curr_node.student.first == first) and (curr_node.student.last == last):
            return curr_node
        # Otherwise, recurse through the left and then right child of the current node to try to find desired student
        else:
            result1 = self.__find_name(first, last, curr_node.left)
            result2 = self.__find_name(first, last, curr_node.right)
            if result1 != None:
                return result1
            elif result2 != None:
                return result2
            else:
                return None

    # Check if the tree is empty
    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False
    
    # Prints all students and their information through recursion
    # Errors: KeyError - when attempting to print from an empty tree
    def print_tree(self):
        # Print the IDs of all nodes by inorder traversal
        if self.is_empty() == False:
            print("==============================")
            self.__print_tree(self.root)
        else:
            raise KeyError("KeyError detected: Tree has no information stored")
    
    # Helper function for print_tree() to print with inorder
    # Input: the current node
    def __print_tree(self, curr_node):
        if curr_node is not self.sentinel:
            self.__print_tree(curr_node.left)
            print("External Student ID: " + str(curr_node.id))
            curr_node.student.print_all()
            print("==============================")
            self.__print_tree(curr_node.right)
    
    # Print all student 95-numbers with their node's color through inorder
    def print_with_colors(self):
        self.__print_with_colors(self.root)

    # Helper function for print_with_colors
    # Input: The current node to print
    def __print_with_colors(self, curr_node):
        # Extracts the color of the node and print it in the format -idC- where C is B for black and R for red
        if curr_node is not self.sentinel:
            # Find the color of the node first
            if curr_node.color == "red":
                node_color = "R"
            else:
                node_color = "B"
            
            self.__print_with_colors(curr_node.left)
            print("External Student ID: " + str(curr_node.id))
            self.__print_with_colors(curr_node.right)

    # various
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
    
    # Find and return a node based a 95-number
    # Input: a student's 95 number ID and 
    # Errors: KeyError - when attempting to p-rint from an empty tree
    def find_node(self, id):
        if self.root:
            desired_id = self.__get(id, self.root)
            if desired_id:
                return desired_id
            else:
                return None
        else:
            raise KeyError("KeyError detected: Tree has no root")

    # Helper function for find_node to return the node and student information associated with the given ID
    # Input: A Student's 95-number to search for and the current node to check
    def __get(self, id, current_node):
        # if current_node does not exist return None
        if current_node is self.sentinel: 
            return None
        elif current_node.id == id:
            return current_node
        # recursively call __get with ID and current_node's left
        elif id < current_node.id:
            return self.__get( id, current_node.left)
        # recursively call __get with ID and current_node's right
        else: # ID is greater than current_node.ID
            return self.__get( id, current_node.right )

    # Function to find a node's successor (based on 95-number)
    # input: a student's 95-number
    # Errors: KeyError - trying to find an id's successor when the id does not exist

    def find_successor(self, id):
        # Start by finding the node with the id number
        current_node = self.find_node(id)
        if current_node is self.sentinel:
            raise KeyError("KeyError: node not found")
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
    def insert(self, id, first_name = "", last_name = ""):
        # if the tree has a root
        if self.root:
            # use helper method to add the new node to the tree
            new_node = self.__put(id, first_name, last_name, self.root)
            self.__rb_insert_fixup(new_node)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(id, first_name, last_name, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)
        
    # helper function __put finds the appropriate place to add a node in the tree
    def __put(self, id, first_name, last_name, current_node):
        if id < current_node.id:
            if current_node.left != self.sentinel:
                new_node = self.__put(id, first_name, last_name, current_node.left)
            else: # current_node has no child
                new_node = Node(id, first_name, last_name, parent = current_node, left = self.sentinel, right = self.sentinel )
                current_node.left = new_node
        else: # ID is greater than or equal to current_node's ID
            if current_node.right != self.sentinel:
                new_node = self.__put(id, first_name, last_name, current_node.right)
            else: # current_node has no right child
                new_node = Node(id, first_name, last_name, parent = current_node,left = self.sentinel,right = self.sentinel )
                current_node.right = new_node
        return new_node

    def delete(self, id):
        
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
                    