#!/usr/bin/env python3

def main():
    dice = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == 5 ]
    for item in dice:
        print(item)

if __name__ == "__main__":
    main()
