
from inspect import getmembers, isfunction, isclass
import sys

def writeStub(funList: list, testFile):
    """takes a dictionary of classes and functions
    and writes the test function signatures for them

    Args:
        funList (list): list of functions for a class or module
        testFile (file object): the test file to write to
    """
    for name in funList:
        name = name.capitalize()
        testSig = f'def test{name}():'
        testFile.write(f'@test\n{testSig}\n\tassert False, "test not implemented"\ntest{name}()\n')

    

def createTestFile(fileUnderTest: str):
    testFile = f'test{fileUnderTest.capitalize()}'

    """
    open the testFile and overwrite if
    it already exists
    write import for file under test
    call getFun to get functions
    call writeSig()

    Args:
        fileUnderTest (str): name of the module under test
    """
    with open(testFile, 'w') as testF:
        testF.write('from PythTest import *\n')
        testF.write(f'from {fileUnderTest[:-3]} import *\n')
        funDict = getFun(fileUnderTest[:-3])
        for val in funDict.values():
            writeStub(val, testF)

def getFun(mod):
    """make a dictionary where the key is the class name and the 
        values are a list of it's function names
        dict = {'className':['fun1','fun2', ...], ... : [...]}

        Args:
            mod(str): the name of the module under test
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
