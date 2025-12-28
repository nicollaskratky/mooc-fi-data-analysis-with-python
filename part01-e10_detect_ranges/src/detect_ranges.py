#!/usr/bin/env python3

def detect_ranges(L):
    sorted_L = sorted(L)
    final_list = []
    sqnc_lst = []
    idx_start = 0
    idx_end = 0
    sequence = False

    for i in range(1, len(L)):

        unique = sorted_L[i - 1] #Valor inicial para ser comparado
        if idx_end != 0: #Se o índice final for 0, pegar o último número da sequência
            sqnc_lst = (sorted_L[idx_start], sorted_L[idx_end])
            final_list.append(sqnc_lst)
            idx_start = 0
            idx_end = 0

        if (unique + 1) == sorted_L[i]: #Se o valor anterior for igual ao valor atual da iteração
            sequence = True
            if idx_start == 0:
                idx_start = sorted_L.index(unique)
            else:
                pass

        if (unique + 1) != sorted_L[i]: #Se o valor anterior for diferente do valor atual da iteração
            if sequence == True:
                idx_end = sorted_L.index(unique)
                sequence = False

            elif sequence == False:
                final_list.append(unique)

    return final_list

    
def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(sorted(L))
    print(result)

if __name__ == "__main__":
    main()
