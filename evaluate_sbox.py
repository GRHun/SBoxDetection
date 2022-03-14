import math
from boolean_function import *
#

def get_size(S):
    """返回nxm的S盒的输入位数N,输出位数M
    """
    size = len(S)
    N = int(math.log(size, 2))
    M = len(bin(max(S)).lstrip("0b"))

    return N, M

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

def get_all_bflc(S, N, M):         
    """返回S盒坐标函数的所有非零线性组合
    """
    n = 2 ** M
    res=[]
    # todo: 就是说可以在直接用size吗？为啥设置一个n
    for i in range(1,n):
        booleanfunc_a = []
        for j in range(len(S)):
            # todo: 看到报告里伪代码是1，修改了，不知是否有影响
            if(bin(i&S[j]).count("1")) % 2 ==1:
                booleanfunc_a.append(0)
            else:
                booleanfunc_a.append(1)
        res.append(booleanfunc_a)
    return res

def nonlinearity(S, N, M):
    """
    返回S盒的非线性度nonlinearity
    S盒的非线性度为所有坐标函数的非零线性组合的非线性度的最小值"""
    bflc = get_all_bflc(S,N,M)
    res = []
    for i in bflc:
        res.append(nonliearity_bf(i, N))
    return min(res)

def is_balanced(S, N, M):
    """
    返回S盒是否具有平衡性"""
    bflc = get_all_bflc(S,N,M)
    flag = True
    for i in bflc:
        if not is_bf_balanced(i):
            flag = False
    return flag

def main():
    
    S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    N, M = get_size(S)

    res = get_coordinate_function(S,N,M)

    for i in range(len(res)):
        # print(i,"\t",ANF(res[i])[0])
        print(i,"\t",res[i])

    B = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0]
    print(is_bf_balanced(B))

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