__function_called = False


def function_that_might_fail():
    global __function_called
    __function_called = True
    raise AssertionError("Function has failed")


