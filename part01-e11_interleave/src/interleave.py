#!/usr/bin/env python3

def interleave(*lists):
    current_list = []
    for l1 in zip(*lists):
        current_list.extend(l1)
    return current_list


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
