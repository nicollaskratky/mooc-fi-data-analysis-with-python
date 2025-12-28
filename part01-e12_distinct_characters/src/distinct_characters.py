#!/usr/bin/env python3

def distinct_characters(L):
    d_dict = {}
    for i in L:
        d_dict[i] = len(set(i))
    return d_dict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
