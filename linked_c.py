class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(Node):
	def __init__(self):
		self.head = None

	def add_node(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		print(temp.data,"-----", temp.next)
		if(temp.next == None):
			print("None")
		else:
			temp = temp.next
		while(temp != self.head):
			print(temp.data,"-----", temp.next)
			temp = temp.next


linked = LinkedList()
ch = "y"
while (ch == "y"):
	inp = input("Enter the data:")
	node = Node(inp)
	linked.add_node(node)
	# linked.printList()
	ch = input("Do you want to continue?")

linked.printList()
