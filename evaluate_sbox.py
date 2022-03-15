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
    返回S盒是否具有平衡性
    任意非零的坐标函数的线性组合都是平衡的"""
    bflc = get_all_bflc(S,N,M)
    flag = True
    for i in bflc:
        if not is_bf_balanced(i):
            flag = False
    return flag

def differential_distribution_table(S,N,M):           
    """返回S盒的差分分布表
    格式是列表"""
    # 初始化一个table
    DDT = [[0 for i in range(pow(2,M))] for j in range(pow(2,N))]
    # the table, In is the XOR of the in-going pair, Out is the resulting XOR,
    # the table returns the number of occurences
    for a in range(pow(2,N)):
        for b in range(pow(2,M)):
            for z in range(pow(2,N)):
                p1 = z ^ a
                res = S[p1] ^ S[z]
                if (res == b):
                    DDT[a][b] += 1
    return DDT

def differential_uniformity(S, N, M):
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

def robustness(S,N,M):
    """
    返回S盒的鲁棒性
    𝜂(𝑆) = (1 − 𝜎(𝑆)/2𝑛)(1 − 𝛿(𝑆)/2𝑛)
    要使差分分布表的第一列包含尽可能少的非零元素
    """
    DDT = differential_distribution_table(S,N,M)
    diffuniformity = differential_uniformity(S,M,N)
    sum = 0
    for i in DDT:
        if(i[0] == 0):
            sum += 0
        else:
            sum += 1
    res = (1-sum/(2**N))*(1-diffuniformity/(2**N))
    return res

def rotation_symmetric(S,N,M):
    """ 
    返回S盒是否具有旋转对称性
    rotation_symmetric
    报告中，S盒，如果组成它的每一个单输出布尔函数都满足轮换对称性，那么该 S 盒满足轮换对称性
    """
    #todo 文献！！
    flag = True
    coordinate_func = get_coordinate_function(S,N,M)
    for i in coordinate_func:
        if not is_bf_rotation_symmetric(i):
            flag = False
    return flag

def has_linear_structure(S,N,M):
    """是否有线性结构"""
    bflc = get_all_bflc(S,N,M)
    for i in bflc:
        if has_bf_linear_structure(i) ==True:
            return True
    return False

def main():
    
    # S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    S = [12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]
    N, M = get_size(S)

    #* 坐标函数测试
    # res = get_coordinate_function(S,N,M)
    # for i in range(len(res)):
    #     # print(i,"\t",ANF(res[i])[0])
    #     print(i,"\t",res[i])
    
    #* 差分分布表测试
    # res = differential_distribution_table(S,N,M)
    # for i in res:
    #     print(i)

    #* 布尔函数测试
    B = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0]
    # print(is_bf_balanced(B))

    #* 是否有线性结构测试
    print(has_linear_structure(S,N,M))

    print("\ndone.")



if __name__ == "__main__":
    main()