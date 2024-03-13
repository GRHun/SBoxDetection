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
        return: 装着m个长为2^N的list，坐标函数(真值表)
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

def nonzero_bflc(S, N, M):
    """返回S盒坐标函数的所有非零线性组合,也称non-trivial component functions
    """
    n = 2 ** M
    res=[]
    for i in range(1,n):
        booleanfunc_a = []
        for j in range(len(S)):
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
    bflc = nonzero_bflc(S,N,M)
    res = []
    for i in bflc:
        res.append(nonliearity_bf(i))
    return min(res)

def is_balanced(S, N, M):
    """
    返回S盒是否具有平衡性
    任意非零的坐标函数的线性组合都是平衡的"""
    bflc = nonzero_bflc(S,N,M)
    flag = True
    for i in bflc:
        if not is_bf_balanced(i):
            flag = False
    return flag

def differential_distribution_table(S,N,M):           
    """返回S盒的差分分布表
    格式是列表
    """
    # 初始化一个2^n x 2^m 的表格
    DDT = [[0 for i in range(2**M)] for j in range(2**N)]
    # 满足𝑆(𝑥)+𝑆(𝑥+𝛼)=𝛽，其中𝛼，𝛽分别是行数和列数的bin
    for a in range(2**N):
        for b in range(2**M):
            for x in range(2**N):
                res = S[x^a] ^ S[x]
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

def linear_approximation_table(S,N,M):
    """
    返回S盒的线性逼近表
    """
    # 初始化一个2^n x 2^m 的table
    LAT = [[0 for i in range(2**M)] for j in range(2**N)]
    for i in range(2**N):
        for j in range(2**M):

            count = 0
            for k in range(len(S)):
                in_masked = k & i
                out_masked = S[k] & j
                if(bin(in_masked).count("1")+bin(out_masked).count("1")) % 2 == 0:
                    count += 1
            res = count - (len(S)//2)
            LAT[i][j] = res

    return LAT

def robustness(S,N,M):
    """
    返回S盒的鲁棒性
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

def is_rotation_symmetric(S,N,M):
    """ 
    返回S盒是否具有旋转对称性
    rotation_symmetric
    报告中，S盒，如果组成它的每一个单输出布尔函数都满足轮换对称性，那么该 S 盒满足轮换对称性
    """
    flag = True
    coordinate_func = get_coordinate_function(S,N,M)
    for i in coordinate_func:
        if not is_bf_rotation_symmetric(i):
            flag = False
    return flag

def has_linear_structure(S,N,M):
    """是否有线性结构"""
    bflc = nonzero_bflc(S,N,M)
    for i in bflc:
        if has_bf_linear_structure(i) ==True:
            return True
    return False

def get_diff_branch_number(S,N,M):
    """返回S盒的差分分支数 differential branch number"""
    # min{wt(a) +wt(b)|δS(a,b)!=0, a∈Fn2\{0}, b∈Fm2}.
    DDT = differential_distribution_table(S,N,M)
    res = []
    for i in range(1, 2**N):
        for j in range(1, 2**M):
            if DDT[i][j] != 0:
                tmp = str(bin(i)).count('1') + str(bin(j)).count('1')
                res.append(tmp)
    return min(res)

def linear_branch_number(S,N,M):
    """返回S盒的线性分支数"""
    LAT = linear_approximation_table(S,N,M)
    res = []
    for i in range(1, 2**N):
        for j in range(0, 2**M):
            if LAT[i][j] != 0:
                tmp = str(bin(i)).count('1') + str(bin(j)).count('1')
                res.append(tmp)
    return min(res) 

def boomerang_connectivity_table(S,N):
    """返回S盒的回旋镖相关表,优化版
    """
    # BCT = [[0 for i in range(2**N)] for j in range(2**N)]
    # for a in range(2**N):
    #     for b in range(2**N):
    #         for x in range(2**N):
    #             tmp1 = S.index(S[x] ^ b)
    #             tmp2 = S.index(S[x ^ a] ^ b)
    #             res = tmp1 ^ tmp2
    #             if (res == a):
    #                 BCT[a][b] += 1
    bct1 = []
    for out in range(2**N):
        T = [[] for i in range(2**N)]
        for x in range(2**N):
            left  = x ^ (S.index(S[x]^out))
            T[left].append(x)

        need = []
        col = [0 for i in range(2**N)]
        for ele in T:
            if len(ele) != 0:
                need.append(ele)

        for ele in need:
            for i in range(len(ele)):
                for j in range(len(ele)):
                    tmp = ele[i]^ele[j]
                    col[tmp] += 1
        bct1.append(col)
    bct = list(map(list,zip(*bct1)))
    return bct

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

def SAC_table(S,N,M):
    """返回S盒的完全雪崩准则概率表
    """
    result =[[0 for i in range(M)] for j in range(N)]
    # 对第i 位取补, 计算第j位的输出的取补的概率
    # 对于每一个输入比特取补，mask=00000001 00000010 00000100...
    # 对第i位取补, 输出的f(x+ei)+f(x) 为结果testval.0<=i<n
    for i in range(N):
        mask = 2**i
        for x in range(2**N):  #! 这里修改了范围，我认为x是每一个x
            testval = S[x]^S[x^mask]
            # testval里，如果第i位是1，就是取补了
            # 对第j位输出，如果在i位输入取补时改变了，那么+1
            for j in range(M):
                # 将结果右移j位，和1相与，如果在i位输入取补时，第j位输出改变了就+1
                bitval = (testval>>j)&1
                result[i][j]+=bitval
        #* 注意：这里的i，j行列排列都是0->i-1，和文献AES中列数排列是相反的

    for i in range(N):
        for j in range(M):
            result[i][j] /=(2**M)
    return result
    
def term_number_distribution(S,N,M):
    # N,M = get_size(S)
    cbf = get_coordinate_function(S,N,M)
    termnum = []
    for i in cbf:
        (a,b) = ANF(i)
        termnum.append(a.count("+")+1)
    return termnum

def autocorrelation_table(S,N,M):
    # 初始化一个2^n x 2^m 的table
    # ACT = [[0 for i in range(2**M)] for j in range(2**N)]
    res = []
    bflc = nonzero_bflc(S,N,M)
    zerofunc = [0 for i in range(2**N)]
    all_linear_comb = []
    all_linear_comb.append(zerofunc)
    for i in bflc:
        all_linear_comb.append(i)
    
    for i in all_linear_comb:
        res.append(autocorrelation(i))
    act = list(map(list,zip(*res)))
    return act

def choose_bf(S,string):         
    """
    返回所选择的S盒特定组成函数的线性组合 如返回x0+x1+x2
    """
    size = len(S)
    M = int(math.log(size, 2))
    N = len(bin(max(S)).lstrip("0b"))
    n = 2 ** N
    temp = string.lower().split("+")
    choose = []
    for i in temp:
        choose.append(int(i.lstrip('x')))
    num = 0
    for i in choose:
        num += 2**i
    booleanfunc = []
    for j in range(size):
        if(bin(num&S[j]).count("1")) % 2 ==0:
            booleanfunc.append(0)
        else:
            booleanfunc.append(1)
    return (booleanfunc,num)

def binary(num, length):            
    """ 将输入数字转化成指定bits长的数据
    """
    binary_string_list = list(format(num, '0{}b'.format(length)))
    return "".join(binary_string_list)

def diffusion(S,N,M):
    allcomponentbf = get_coordinate_function(S,N,M)
    aset = set_a(N)
    
    halfN = (2**N)/2
    k = []
    for i in allcomponentbf:
        flag=0
        break_ = 0
        for a in aset:
            for ai in a:
                temp = []
                for j in range(2**N):
                    temp.append(i[j^ai]^i[j])
                if temp.count(1)!=halfN:
                    k.append(flag)
                    break_ = 1
                    break
            if break_==1:
                break
            flag += 1
        else:
            k.append(flag)
    return min(k)

def set_a(N):       #将所有向量a进行分组
    result=[]
    result2=[]
    a1 = []
    for i in range(N):
        a1.append(2**i)
    result.append(a1)
    for i in range(N-1):
        usea = result[i]
        temp = []
        for j in usea:
            for k in a1:
                tempi = binary(j^k,N)
                if tempi.count("1")==i+2:
                    temp.append(int(tempi,2))
                else:
                    pass
        result.append(list(set(temp)))
    return result

def degree(S,N,M):
    """返回最大代数次数和一致代数次数"""
    bflc = nonzero_bflc(S,N,M)
    degree_lis = []
    for i in bflc:
        deg = ANF(i)[1]
        degree_lis.append(deg)
    return max(degree_lis),min(degree_lis)


def main():
    
    # S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    # S = [12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]
    S = [14, 9, 15, 0, 13, 4, 10, 11, 1, 2, 8, 3, 7, 6, 12, 5]
    N, M = get_size(S)

    #* 扩散测试、
    # k = diffusion(S,N,M)
    # print(k) 

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
    # B = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0]
    # print(is_bf_balanced(B))

    #* 是否有线性结构测试
    # print(has_linear_structure(S,N,M))

    #* 计算BCT表
    # bct = boomerang_connectivity_table(S,N)
    # for i in bct:
    #     print(i)

    # *鲁棒性
    AES=[
    0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
    0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
    0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
    0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
    0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
    0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
    0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
    0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
    0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
    0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
    0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
    0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
    0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
    0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
    0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
    0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16]

    print(robustness(AES,8,8))

    print("\nAll computing is done.")

if __name__ == "__main__":
    main()