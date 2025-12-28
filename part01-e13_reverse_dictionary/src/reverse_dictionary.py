#!/usr/bin/env python3

def reverse_dictionary(d):
    reverse = {}
    for key, value in d.items():
        for item in value:
            if item not in reverse:
                reverse[item] = []
            reverse[item].append(key)

    return reverse

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
