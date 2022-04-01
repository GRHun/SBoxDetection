from get_all_bflc import get_all_bflc
from get_size import get_size

def inverse_S(x, S):
    return S.index(x)

def boomerang_connectivity_table(S,N):
    """返回S盒的回旋镖相关表  N->N
    暂时用定义写的"""
    BCT = [[0 for i in range(2**N)] for j in range(2**N)]
    for a in range(2**N):
        for b in range(2**N):
            for x in range(2**N):
                res = S.index(S[x] ^ b) ^ S.index(S[x ^ a] ^ b)
                if (res == a):
                    BCT[a][b] += 1
    return BCT


def main():
    S = [3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    N, M = get_size(S)
    # print(M,N)
    # print(inverse_S(15,S))

    x = boomerang_connectivity_table(S,N)
    for i in x:
        print(i)

if __name__ == "__main__":
    main()

