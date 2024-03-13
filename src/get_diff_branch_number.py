from get_size import get_size
from differential_distribution_table import differential_distribution_table

def get_diff_branch_number(S,N,M):
    """返回S盒的差分分枝数 differential branch number"""

    # min{wt(a) +wt(b)|δS(a,b)!=0, a∈Fn2\{0}, b∈Fm2}.
    DDT = differential_distribution_table(S,N,M)
    res = []
    for i in range(1, 2**N):
        for j in range(1, 2**M):
            if DDT[i][j] != 0:
                tmp = str(bin(i)).count('1') + str(bin(j)).count('1')
                res.append(tmp)
    return min(res)



def main():
    # S=[12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]
    # S = [3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    # S = [7,6,0,4,2,5,1,3]
    S=[27,50,51,90,59,16,23,84,91,26,114,115,107,44,102,73,31,36,19,108,55,46,63,74,93,15,64,86,37,81,28,4,11,70,32,13,123,53,68,66,43,30,65,20,75,121,21,111,14,85,9,54,116,12,103,83,40,10,126,56,2,7,96,41,25,18,101,47,48,57,8,104,95,120,42,76,100,69,117,61,89,72,3,87,124,79,98,60,29,33,94,39,106,112,77,58,1,109,110,99,24,119,35,5,38,118,0,49,45,122,127,97,80,34,17,6,71,22,82,78,113,62,105,67,52,92,88,125]
    N, M = get_size(S)
    print(get_diff_branch_number(S,N,M))


if __name__ == "__main__":
    main()

