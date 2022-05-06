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
        # print("坐标函数",i,"\tautocorrelation:",autocorrelation(i))
        res.append(autocorrelation(i))

    return res
    

def main():
    # S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    S = [7,6,0,4,2,5,1,3]
    N, M = get_size(S)
    act = autocorrelation_table(S,N,M)
    act1 = list(map(list,zip(*act)))
    for i in act1:
        print(i)
    


if __name__ == "__main__":
    main()

