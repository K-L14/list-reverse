# list_reverse.py

def reverse_list(a):
    """
    Reverses a given list in place.

    Args:
    a (list): The list to be reversed.

    Returns:
    list: The reversed list.
    """
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    
    N = len(a)
    for i in range(len(a) // 2):
        a[i], a[N - i - 1] = a[N - i - 1], a[i]
    return a

if __name__ == '__main__':
    # Example usage
    a = [9, 7, 5, 3, 1]
    print("Original list:", a)
    reversed_list = reverse_list(a)
    print("Reversed list:", reversed_list)
