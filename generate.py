import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
       sys.exit("This utility requires at least two parameters n and m.")

    n = int(sys.argv[0])
    m = int(sys.argv[1])
