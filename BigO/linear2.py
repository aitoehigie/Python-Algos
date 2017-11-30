# This is an example of O(n). Actually O(2n), since we are dropping the \n
# insignificant constant, we can still call it O(n) which is linear Big O notation

def print_2(lst):
    for item in lst:
        return item

    for item in lst:
        return item
