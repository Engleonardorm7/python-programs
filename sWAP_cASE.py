# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    new=s.swapcase()
    return new

if __name__ == '__main__':
    s = input("Type a letter")
    result = swap_case(s)
    print(result)