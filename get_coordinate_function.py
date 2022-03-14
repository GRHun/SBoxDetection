import math
#
from ANF import ANF
from get_size import get_size

def get_coordinate_function(S,N,M):
    """返回S盒的m个坐标函数coordinate function
        para: N输入， M输出
        return: 元素为m个坐标函数(真值表)的list
    """

    res=[]
    for i in range(M):
        index = 1<<i  # index=0001 0010 0100 1000 与S盒相与即可提取出其布尔函数
        coordinate_func = []
        # 对每一个输入j，比如S(0)=3，S(1)=8 => S(0000)=0011,S(0001)=1000
        # 取出第i处的值，加入到输入为j时对应的位置
        for j in range(len(S)):
            coordinate_func.append(bin(index&S[j]).count("1"))
        res.append(coordinate_func)
    return res


def main():
    
    S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    N, M = get_size(S)

    res = get_coordinate_function(S,N,M)

    for i in range(len(res)):
        # print(i,"\t",ANF(res[i])[0])
        print(i,"\t",res[i])

    """ test
    input:
    S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    output:
    0   [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0]
    1   [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0]
    2   [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1]
    3   [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
    """


if __name__ == "__main__":
    main()