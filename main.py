import sys
#kaushik jaiswal 14/07/2020
#Tinkori Nath Bose Lane 
from linux_file_traversal import PathStructure


commands = ["cd","mkdir","rm","pwd","ls"]

sys.stdout.write("$ <Starting your application....>\n")

tree = PathStructure()


while True:
	cmd = input("$ ")

	if cmd == "session clear":
		tree = PathStructure()
		print("SUCC: CLEARED : RESET TO ROOT")
		continue

	print(tree.command_process(cmd))