import sys
import argparse
#2
s=0
if len(sys.argv)>1:
    for i in range(1,len(sys.argv)):
        s+=int(sys.argv[i])*-1**i+1
       
    print(s)
else:
    print("Error")
print("")

