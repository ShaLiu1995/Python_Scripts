import os
import sys

def show_dir_tree(dir='.'):
	for root, dirs, files in os.walk(dir):
		path = root.split(os.sep)
		print((len(path) - 1) * '---', os.path.basename(root))
		for file in files:
			print(len(path) * '---', file)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		show_dir_tree(sys.argv[1])
	else:
		show_dir_tree()