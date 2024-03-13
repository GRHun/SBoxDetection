from get_size import get_size
from  boomerang_connectivity_table import boomerang_connectivity_table

def boomerang_uniformity(S,N):
    """
    返回差分均匀度
    """
    BCT = boomerang_connectivity_table(S,N)
    # 去掉第一行第一列
    del BCT[0]
    for i in BCT:
        i[0] = 0

    res = []
    for i in BCT:
        res.append(max(list(map(abs,i))))
    return max(res)


def main():
    # S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    S = [1,13,15,0,14,8,2,11,7,4,12,10,9,3,5,6]
    N, M = get_size(S)
    a = boomerang_uniformity(S,N)
    print(a)

    # for i in a:
    #     print(i)



if __name__ == "__main__":
    main()

