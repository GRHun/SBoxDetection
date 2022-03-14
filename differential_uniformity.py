from get_size import get_size
from differential_distribution_table import differential_distribution_table

def differential_uniformity(S,M,N):
    """
    返回差分均匀度
    """
    DDT = differential_distribution_table(S,N,M)
    # 非零差分，所以第一个手动去掉
    DDT[0][0]=0
    result=[]
    for i in DDT:
        result.append(max(list(map(abs,i))))
    return max(result)


def main():
    # S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    S = [1,13,15,0,14,8,2,11,7,4,12,10,9,3,5,6]
    N, M = get_size(S)
    print(differential_uniformity(S,M,N))


if __name__ == "__main__":
    main()

