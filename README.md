# PythonTestMaker
Prototype unit test writer for python
# But Why?
As far as I can tell no one really asked for this or needs it, there are other testing modules out there that work great, but this one is mine.
# So you must have a lot of python code to test, right?
Nope, this is actually the most useful thing I've ever written in python. I don't even have hidden repos that might require unit testing.
# SO WHY THEN!!!!!
I want to get hired.
# How to Use it right now
to make a test file:
python -m PythTest create factorial.py

to run it:
python testFactorial.py

eventually I'll make a runner which will call all of the test functions individually in setup->test->teardown order (like JUnit)
