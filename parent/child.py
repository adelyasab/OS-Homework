#!/usr/bin/python3
import os
import random 
import sys
import time

print("Child process started. Pid ", os.getpid(), " with argument  ", sys.argv[1])
time.sleep(int(sys.argv[1]))
print("Pid of ChP: ", os.getpid(), " finished")
exit(random.choice([0, 1]))
