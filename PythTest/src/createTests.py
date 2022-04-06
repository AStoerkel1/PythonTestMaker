
def writeSig(line: str, testFile):
    """
    isolates the function signature and 
    writes it to a new file

    TO-DO: eventually I will write a runner which will call
    all of the tests instead of calling them from 
    inside the test file
    
    Args:
        line (str): line with a function signature in it
    """
    signature = line.split()[-1].capitalize()
    endOfName = signature.find('(')
    name = signature[:endOfName]
    testSig = f'def test{name}():'
    testFile.write(f'@test\n{testSig}\n\tassert False, "test not implemented"\ntest{name}()')

    

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
        for l in lines: 
            if l.strip().startswith('def'):
                writeSig(l, testF)           


