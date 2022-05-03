from boolean_function import nonliearity_bf
from get_all_bflc import get_all_bflc
#
from get_size import get_size


def nonlinearity(S, N, M):
    """返回S盒的非线性度
        S盒的非线性度为所有坐标函数的非零线性组合的非线性度的最小值"""
    bflc = get_all_bflc(S,N,M)
    res = []
    for i in bflc:
        res.append(nonliearity_bf(i))
    return min(res)

def main():
    S = [3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    N, M = get_size(S)
    print("N,M:", N,M)
    print(nonlinearity(S,N,M))


if __name__ == "__main__":
    main()

