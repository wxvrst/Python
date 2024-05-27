import sys
import argparse
#1
#if len(sys.argv)==2:
#    print(int(sys.argv[1])+int(sys.argv[2]))
#else:
#    print("Error")

#2
s=0
if len(sys.argv)>1:
    for i in range(1,len(sys.argv)):
        print(f"Key: {sys.argv[i][:str(sys.argv).find('=')]}")
        print(f"Value: {sys.argv[i][str(sys.argv).find('='):]}")
    print(s)
else:
    print("Error")
print("")

