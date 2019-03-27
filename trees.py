class Tree_node():
	def __init__(self, data, children=None):
		self.data=data
		self.children=[]
		if children:
			self.children.extend(children)

* Given a tree Node class, write a method that returns the number of nodes in the tree.
	def number_nodes(self):
		current= [self]
		count = 0
		while current != []:
			count += 1
			x =current.pop(0)
			current.extend(x.children)
		return count

* Given a tree Node class, write a method that returns True if any nodes in the tree have duplicate data.
	def if_duplicate(self):
		current = [self]
		seen = set()
		while current != []:
			check = current.pop(0)
			if check.data in seen:
				return True
			else:
				seen.add(check)
				current.append(check.children)
		return False

* Given a tree Node class, write a method that takes an item as its only parameter and returns True if the data for any node in the tree matches the given item.
	def if_item(self, item):
		current=[self]
		while current != []:
			check = current.pop(0)
			if check.data == item:
				return True (for question below return check)
			else:
				current.append(check.children)
		return False

* Given a tree Node class, write a method that takes an item as its only parameter and returns the highest ranking node whose data matches the given item. (Alternate: return the lowest ranking item.) DID highest ranking node above (BFS), sO NOW doing DFS
	def if_item(self, item):
		current=[self]
		while current != []:
			check = current.pop()
			if check.data == item:
				return check
			else:
				current.append(check.children)
		return False
	
* Given a tree Node class, write a method that takes an item and a node as its two parameters, and adds the node to the first node in the tree whose data matches the given item. (You may assume that there are no nodes with duplicate data in the tree, or you may decide to define “first node” using breadth-first or depth-first search, or your interview may decide for you).
	def add_nodes(self, item, node):
		current = [self]
		while current != []:
			check = current.pop(0)
			if check.data == item:
				check.children.append(node)
			else:
				current.append(check.children)


* Given a BinarySearchNode class, write a method that takes an item as its only parameter and returns the node in the BST whose data matches the given parameter.
	def if_item(self, item):
		current = self
		while current != None:
			if current.data == item:
				return current
			else:
				if item < current.data:
					current = current.left
				else:
					current = current.right
		return None
		

* Given BinarySearchNode class, write a method that returns the total number of nodes in the tree.

* [Harder] Given a tree Node class, write a method that takes an item as its only parameter and removes any nodes in the tree whose data matches the given item. Question: what happens to the deleted node’s children?
* [Harder] Given a BinarySearchNode class, write a method to insert a node into the BST at its proper location.
