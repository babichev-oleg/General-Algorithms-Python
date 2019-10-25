#!/usr/bin/python3.6
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

s = "0123456789"
if __name__ == "__main__":
    print ("The original string  is : ",end="")
    print (s)
    print ("The reversed string(using loops) is : ",end="")
    print (reverse(s))

