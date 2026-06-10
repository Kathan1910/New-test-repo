"""
abc.py

A minimal module created per request. Provides a tiny, import-safe function and
a runnable entry point.
"""


# PUBLIC_INTERFACE
def hello_from_abc() -> str:
    """Return a short greeting string from abc.py."""
    return "Hello from abc.py!"


if __name__ == "__main__":
    print(hello_from_abc())
