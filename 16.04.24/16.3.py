import sys
import argparse
#3
if len(sys.argv)>1:
    if sys.argv[3]=='-':
        print(float(sys.argv[1]) - float(sys.argv[2]))
        
    elif sys.argv[3]=='+':
        print(float(sys.argv[1]) + float(sys.argv[2]))
        
    elif sys.argv[3]=='/':
        print(float(sys.argv[1]) / float(sys.argv[2]))
        
    elif sys.argv[3]=='*':
        print(float(sys.argv[1]) * float(sys.argv[2]))

    
else:
    print("Error")
print("")

