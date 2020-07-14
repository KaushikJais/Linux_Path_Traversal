class Node(object):

	#Written by Kaushik Jaiswal

	"""
		Each Tree Node contains two data members

		Name: Name of the Directory

		children: List of the directories in a directory

	"""

	def __init__(self,name):

		self.name = name
		self.children = []


class PathStructure(object):

	"""

		root : Tree Node having a root directory

		current_path : List containing all the node which represents path from root directory

		pointer : pointer to a current directory in file structure
	"""
	def __init__(self):


		self.root = Node('/')
		self.current_path = []
		self.pointer = self.root

	def do_pwd(self):


		""" This method returns the path of current directory from root directory """

		if self.pointer == self.root:
			return "PATH:" + self.pointer.name

		s = "/"

		return "PATH: /" + s.join(self.current_path)

	def command_process(self, cmd: str):

		""" This method process input command from user and,
		    based on command different method gets invoked by this method 
		"""


		if cmd == 'pwd':
			return self.do_pwd()

		cmd = cmd.strip().split()

		if cmd[0]  == 'ls':
			return self.list_dir()

		elif cmd[0] == 'mkdir':
			return self.make_new_dir(cmd[1])

		elif cmd[0] == 'cd':
			return self.change_dir(cmd[1])

		elif cmd[0] == 'rm':
			return self.remove_dir(cmd[1])

		elif cmd[0].endswith('dir'):
			return self.list_dir(cmd)

		else :
			return "ERR: CANNOT RECOGNIZE THE INPUT"

	def list_dir(self, cmd = None):


		"""
			This methos return the list of all directory present in the current directory.
		"""

		children = []
		start = "DIRS: "


		if cmd:
			dirs = cmd[0].split('/')
			node = self.pointer

			for char in dirs[:-1]:

				flag = False

				for child in node.children:
					if child.name == char:
						flag = True
						node = child
						break


			if not flag:
				return "ERR: INVALID PATH"

			for child in node.children:

				children.append(child.name)

		else:

			for child in self.pointer.children:
				children.append(child.name)

		return start + " ".join(children)


	def make_new_dir(self, word):


		"""
			This method adds a new directory (if not present) in the current directory
		"""

		word = word.strip().split('/')

		if len(word) == 1:

			
			for child in self.pointer.children:

				if child.name == word[0]:
					return "ERR: DIRECTORY ALREADY EXIST"

			new_node = Node(word[0])
			self.pointer.children.append(new_node)
			return "SUCC: CREATED"

		node = self.pointer
		count = 0

		for char in word[1:]:
			flag = False

			for child in node.children:

				if child.name == char:
					count+=1
					node = child
					flag = True
					break

			if not flag and count == 0 :
				new_node = Node(char)
				node.children.append(new_node)
				count+=1
				break

		if not flag and count == len(word)-1:
			return "SUCC: CREATED"

		return "ERR: DIRECTORY ALREADY EXIST"

	def change_dir(self, word):


		"""
			This method return whether file structure can be traverse
        	through a particular path.
		"""

		if word == '/':

			self.pointer = self.root
			self.current_path = []
			return "SUCC: REACHED"

		word = word.strip().split('/')

		if len(word) == 1 : 

			for child in self.pointer.children:

				if child.name == word[0]:
					self.pointer = child
					self.current_path.append(child.name)
					return "SUCC: REACHED"

			return "ERR: INVALID PATH"

		curr = self.current_path
		node = self.pointer

		for char in word[1:]:
			flag = False

			for child in node.children:

				if child.name == char :
					flag = True
					curr.append(child.name)
					node = child
					break

			if not flag:
				return "ERR: INVALID PATH"

		self.current_path = curr
		self.pointer = node

		return "SUCC: REACHED"

	def remove_dir(self , word):


		"""
			This method is required to delete or remove a directory
		"""
		word = word.strip().split('/')

		if len(word) == 1:
			for child in self.pointer.children:

				if child.name == word[0]:
					self.current_path.pop(child.name)
					return "SUCC: DELETED"

			return "ERR: INVALID PATH"

		curr = self.current_path
		node = self.pointer
		count = 0

		for char in word[1:]:

			flag = False

			for child in node.children:

				if child.name == char:
					flag = True
					count+=1
					curr = node
					node = child

				if flag and count == len(word)-1:
					curr.children.remove(child)
					return "SUCC: DELETED"

		return "ERR: INVALID PATH"