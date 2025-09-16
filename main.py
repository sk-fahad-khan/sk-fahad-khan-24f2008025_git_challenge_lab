from sum import add
from difference import subtract
from product import multiply

def main():
    a = 10
    b = 5
    print(f"Sum: {add(a, b)}")
    print(f"Difference: {subtract(a, b)}")
    print(f"Product: {multiply(a, b)}")

if __name__ == "__main__":
    main()
