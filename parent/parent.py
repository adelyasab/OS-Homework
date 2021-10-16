#!/usr/bin/python3
import os
import random
import sys

child = 1
n = int(sys.argv[1])
for i in range(n):
	if child == 0:
		break
	child = os.fork()
if child > 0 :
	for i in range(0, n):
		ret = os.wait()
		print("Child process ", ret[0], "finished. Code: ", ret[1])
else:
	os.execl('child.py', "child.py", str(random.choice(range(5, 11))))
