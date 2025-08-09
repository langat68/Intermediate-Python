

# Example 1: Using *args
def add_numbers(*args):
    """Accepts any number of numbers and returns their sum."""
    print("args received:", args)  # tuple
    return sum(args)
