import sys

from test_helper import run_common_tests, failed, passed, \
    import_task_file


def test_doesnt_crash():
    try:
        import_task_file()
    except AssertionError:
        failed("You didn't catch the exception from the function")
    except Exception:
        passed()  # will be delivered to run_common_tests
    else:
        passed()


def test_function_called():
    if not sys.modules['helper'].__function_called:
        failed("You didn't call function_that_might_fail")
    else:
        passed()


if __name__ == '__main__':
    test_doesnt_crash()
    # order change, so i can catch AssertionError myself.
    # if i will let run_common_tests catch it, it will say syntax error.
    run_common_tests()
    test_function_called()


