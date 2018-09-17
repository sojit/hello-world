#!/usr/bin/python3
#Author: Soji
#version: v1.0
''' 
This script is to conver the symbolic file permission to octal permission 
and the required input for this code is "rwxrwxrwx" or "r-xr-xr-x". 
'''
class symbolicp:

    def __init__(self, read, write, execute):
        self.read = read
        self.write = write
        self.execute = execute

    def read_ugo(self):
        if self.read == "r":
            return 4
        elif self.read == "-":
            return int(0)
 
   def write_ugo(self):
        if self.write == "w":
            return 2
        elif self.write == "-":
            return int(0)

 
   def execute_ugo(self):
        if self.execute == "x":
           return 1
        elif self.execute == "-":
            return int(0)

file_permission = input("Enter the value:")
fp = file_permission.split()
for list in fp:
   user = symbolicp(list[0], list[1], list[2])
   group = symbolicp(list[3], list[4], list[5])
   other = symbolicp(list[6], list[7], list[8])


one = (user.read_ugo() + user.write_ugo() + user.execute_ugo())
two = (group.read_ugo() + group.write_ugo() + group.execute_ugo())
three = (other.read_ugo() + other.write_ugo() + other.execute_ugo())

print("The octal value is:",one,two,three)