from ast import Pass
from get_size import get_size
from boolean_function import *
from get_all_bflc import get_all_bflc

def autocorrelation_table(S,N,M):
    # 初始化一个2^n x 2^m 的table
    # ACT = [[0 for i in range(2**M)] for j in range(2**N)]
    res = []
    bflc = get_all_bflc(S,N,M)
    zerofunc = [0 for i in range(2**N)]
    all_linear_comb = []
    all_linear_comb.append(zerofunc)
    for i in bflc:
        all_linear_comb.append(i)
    
    for i in all_linear_comb:
        res.append(autocorrelation(i))
    act = list(map(list,zip(*res)))
    return act
    
def list2str(table):
    tab_str = ""
    for i in table:
        tab_str += str(i)
        tab_str += "\n"
    print(tab_str)
        

def main():
    S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    # S = [7,6,0,4,2,5,1,3]
    N, M = get_size(S)
    act = autocorrelation_table(S,N,M)

    for i in act:
        print(i)

    print("=========>\n")

    list2str(act)
    


if __name__ == "__main__":
    main()

