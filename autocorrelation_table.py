from get_size import get_size
from boolean_function import *
from get_all_bflc import get_all_bflc

def autocorrelation_table(S,N,M):
    # 初始化一个2^n x 2^m 的table
    # ACT = [[0 for i in range(2**M)] for j in range(2**N)]
    res = []
    bflc = get_all_bflc(S,N,M)
    for i in bflc:
        res.append(autocorrelation(i))

    return res
    

def main():
    # S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    # S = [7,6,0,4,2,5,1,3]
    S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    N, M = get_size(S)
    act = autocorrelation_table(S,N,M)
    for i in act:
        print(i)
    


if __name__ == "__main__":
    main()

