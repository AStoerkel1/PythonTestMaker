
from inspect import getmembers, isfunction, isclass
import sys

def writeSig(funList: list, testFile):
    """takes a dictionary of classes and functions
    and writes the test function signatures for them

    Args:
        functionDict (list): list of functions for a class or module
        testFile (file object): the test file to write to
    """
    for name in funList:
        testSig = f'def test{name}():'
        testFile.write(f'@test\n{testSig}\n\tassert False, "test not implemented"\ntest{name}()\n')

    

def createTestFile(fileUnderTest: str):
    testFile = f'test{fileUnderTest.capitalize()}'
    
    """
    open the file and readlines() as lines
    with does not create scope
    """
    with open(fileUnderTest, 'r') as file:
        lines = file.readlines()

    """
    open the testFile and overwrite if
    it already exists
    write import for wrappers
    look for function signatures
    call writeSig() if one is found

    Args:
        lines (list): list of all the lines
    """
    with open(testFile, 'w') as testF:
        testF.write('from PythTest import *\n')
        testF.write(f'from {fileUnderTest[:-3]} import *\n')
        funDict = getFun(fileUnderTest[:-3])
        for val in funDict.values():
            writeSig(val, testF)

def getFun(mod):
    """make a dictionary where the key is the class name and the 
        values are a list of it's function names
        dict = {'className':['fun1','fun2', ...], ... : [...]}

        Args:
            mod(str): the module to test
    """
    __import__(mod)
    myMod = sys.modules[mod]
    #holds a list of classes as [('className', <object reference>), ...]
    #this line will pick out the members of the imported module and if it is a class add it to the list
    classes = [o for o in getmembers(myMod) if isclass(o[1])]

    #this will build a dictionary where the key is the class name and the value is a list of that class's functions
    #Warning: do not meddle with forces you do not fully understand
    newDict={key:val for (key, val) in zip([c[0] for c in classes],[[f[0] for f in getmembers(c[1]) if isfunction(f[1])] for c in classes])}

    return(newDict)
