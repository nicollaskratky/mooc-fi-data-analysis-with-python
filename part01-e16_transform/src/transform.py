#!/usr/bin/env python3

def transform(s1, s2):
    words1 = s1.split()
    words2 = s2.split()
    words1 = (list(map(lambda x: int(x), words1)))
    words2 = (list(map(lambda x: int(x), words2)))
    final = [word1*word2 for word1, word2 in zip(words1, words2)]
    return final

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
