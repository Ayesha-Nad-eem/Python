def main():
    x = int(input("Enter x:"))
    if is_even(x):
        print("x is Even")
    else: 
        print("x is Odd")

def is_even(n):
    return n % 2 == 0

    # return True if n % 2 == 0 else False # Pythonic expression
    # if n % 2==0:
    #     return True
    # else:
    #     return False
    
main()