"""
This program is to apply learnings of os module
"""
import os
import time

print(os.getcwd())

PARENT_DIR = "D:/H/Work/Genesis/99004510-advance python/practise"
DIR_NAME = "Test directory"

path = os.path.join(PARENT_DIR, DIR_NAME)

os.mkdir(path)

time.sleep(25)

os.rmdir(path)
