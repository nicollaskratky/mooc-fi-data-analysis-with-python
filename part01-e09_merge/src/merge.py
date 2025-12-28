#!/usr/bin/env python3

def merge(L1,L2):
    l1_cont = 0
    l2_cont = 0
    final_list = []

    while l1_cont < len(L1) or l2_cont < len(L2):
        if l2_cont == len(L2):
            final_list.append(L1[l1_cont])
            l1_cont += 1
        
        elif l1_cont == len(L1):
            final_list.append(L2[l2_cont])
            l2_cont += 1

        elif L1[l1_cont] < L2[l2_cont]:
            final_list.append(L1[l1_cont])
            l1_cont += 1
        else:
            final_list.append(L2[l2_cont])
            l2_cont +=1
    return final_list


def main():
    result = merge([1, 5, 9, 12], [2, 6, 10])
    print(result)
    pass

if __name__ == "__main__":
    main()
