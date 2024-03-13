from evaluate_sbox import linear_approximation_table
from get_size import get_size


def linear_branch_number(S,N,M):
    LAT = linear_approximation_table(S,N,M)
    res = []
    for i in range(1, 2**N):
        for j in range(0, 2**M):
            if LAT[i][j] != 0:
                tmp = str(bin(i)).count('1') + str(bin(j)).count('1')
                res.append(tmp)
    return min(res)      
   
def main():
    S = [12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]
    # S= [0x4,0x0,0x1,0xF,0x2,0xB,0x6,0x7,0x3,0x9,0xA,0x5,0xC,0xD,0xE,0x8]
    N,M = get_size(S)
    print(linear_branch_number(S,N,M))
    

if __name__ == "__main__":
    main()