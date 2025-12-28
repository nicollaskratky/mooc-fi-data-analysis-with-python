#!/usr/bin/env python3

def find_matching(L, pattern):
    final_list = []
    for i, x in enumerate(L):
        if pattern in x:
            final_list.append(i)

    return final_list

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
