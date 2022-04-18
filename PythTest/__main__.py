from .src.createTests import createTestFile
import sys
import os

#save the present working directory
PWD = os.getcwd()
#add PWD to system path
if PWD not in sys.path:
    sys.path.append(PWD)

def main():
    command = sys.argv[1]
    if(command == 'create'):
        createTestFile(sys.argv[2])
    if(command == 'run'):
        """
        everything below here should go in the runner
        which still needs to be made
        testRunner()
        """
        for i in os.listdir():
            if i.__contains__("test"):
                with open(i, 'r') as f:
                    exec(f.read())
