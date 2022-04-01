import functools


def backoption_error():
    raise Exception("No back option method passed")

def backoption(f=None, *, back_method=backoption_error):

    if f is None:
        return lambda f : backoption(f, back_method=back_method)

    @functools.wraps
    def inner(*args, **kwargs):
        res = f(*args, **kwargs)
        if res == "Back":
            return back_method()
        return res
    return inner

