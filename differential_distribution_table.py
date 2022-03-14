from get_size import get_size

def differential_distribution_table(S,N,M):           
    """返回S盒的差分分布表
    格式是列表
    """
    # 初始化一个2^n x 2^m 的表哥 
    DDT = [[0 for i in range(2**M)] for j in range(2**N)]
    # 满足𝑆(𝑥)+𝑆(𝑥+𝛼)=𝛽，其中𝛼，𝛽分别是行数和列数的bin
    for a in range(2**N):
        for b in range(2**M):
            for x in range(2**N):
                res = S[x^a] ^ S[x]
                if (res == b):
                    DDT[a][b] += 1
    return DDT

def main():
    # S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    # DES_S0=[14, 0, 4, 15, 13, 7, 1, 4, 2, 14, 15, 2, 11, 13, 8, 1, 3, 10, 10, 6, 6, 12, 12, 11, 5, 9, 9, 5, 0, 3, 7, 8, 4, 15, 1, 12, 14, 8, 8, 2, 13, 4, 6, 9, 2, 1, 11, 7, 15, 5, 12, 11, 9, 3, 7, 14, 3, 10, 10, 0, 5, 6, 0, 13]
    # S=[7,6,0,4,2,5,1,3]
    S = [1,13,15,0,14,8,2,11,7,4,12,10,9,3,5,6]
    N, M = get_size(S)
    res = differential_distribution_table(S,N,M)
    for i in res:
        print(i)


if __name__ == "__main__":
    main()