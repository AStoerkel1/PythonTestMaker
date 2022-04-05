def test(func):
    """
    try to run the function then print
    passed or catch the assertion error and 
    print it with failure message

    Args:
        func (function): test function
    """
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print(f'{func.__name__} passed')
        except AssertionError as e:
            print(f'{func.__name__} failed: {e}')
    return wrapper