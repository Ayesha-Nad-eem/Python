#loops
# i=3
# while i != 0:
#     print("meow")
#     i-=1

# for _ in range(3):
#     print("meow")

def main():
    n=get_input()
    meow(n)

def get_input():
    while True: 
        n=int(input("Enter a number: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()