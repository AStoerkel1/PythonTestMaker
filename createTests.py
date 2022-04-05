"""
TO-DO: 
1. get file as an argument
"""
FILE_UNDER_TEST = 'factorial.py'
TEST_FILE = f'test{FILE_UNDER_TEST.capitalize()}'

def writeSig(line: str):
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
    testFile.write(f'@test\n{testSig}\n\tassert False, "not implemented"\ntest{name}()')

"""
open the file and readlines() as lines
with does not create scope
"""
with open(FILE_UNDER_TEST, 'r') as file:
    lines = file.readlines()

"""
open the testFile and overwrite if
it already exists
write import for wrappers
look for function signatures
call writeSig() if one is found
"""
with open(TEST_FILE, 'w') as testFile:
    testFile.write('from pythWrappers import *\n')
    for l in lines: 
        if l.__contains__('def'):
            writeSig(l)
            

