import math

def get_n(v): 
    """返回布尔函数的元数/输入位数"""
    n = int(math.log(len(v), 2))
    return n

def fwt(v): 
    """
    快速Walsh变换，返回walsh spectrum
    para:v 是布尔函数的真值表(0/1)
    eg  :v = [0,1,0,0,0,1,1,1]
         wht = [0, 4, 0, 4, 4, 0, -4, 0]
    """
    wht = []
    for x in v:
        if x == 0:
            wht.append(1)
        else:
            wht.append(-1)

    # order = len(v)  # order = 2^n
    # n = int(math.log(order, 2))
    # # size = int(math.floor(order / 2))

    # for i in range(1,n+1,1):
    #     m=2**i
    #     halfm=2**(i-1)
        
    #     for k in range(0,order,m):
    #         t1=k
    #         t2=k+halfm
    #         for p in range(halfm):
    #             a = wht[t1]
    #             b = wht[t2]
    #             wht[t1] = a + b
    #             wht[t2] = a - b
    #             t1 = t1 + 1
    #             t2 = t2 + 1
    # return wht


    h = 1
    while h < len(wht):
        for i in range(0, len(wht), h * 2):
            for j in range(i, i + h):
                x = wht[j]
                y = wht[j + h]
                wht[j] = x + y
                wht[j + h] = x - y
        h *= 2
    return wht

def binary(num, length):            
    """将输入数字转化成指定bits长的数据
    """
    binary_string_list = list(format(num, '0{}b'.format(length)))
    return "".join(binary_string_list)

def ANF(v):             
    """函数返回布尔函数的字符串格式代数标准形式和代数次数deg f
    param: v - 布尔函数的真值表
    e.g. : v = [0,1,0,0,0,1,1,1]
    """
    n = int(math.log(len(v),2))

    for k in range(1, n+1):
        # print("k",k)
        for i in range(2**(n-k)):  # !为什么这里取不到！！！！！为啥
            # print("i",i)
            # Compute the image of the i-th 2k-bit block
            for j in range((2**(k-1))):
                # print("j",j)
                var1 = v[(2**k)*i+j]
                index1 = (2**k)*i+j+(2**(k-1))
                var2 = v[index1]
                v[index1] = (var1 + var2)%2
    # print("V:\t" ,v)

    # 转换成ANF的形式，格式为字符串 ，同时计算algebraic_degree   
    flag, degree = 0, 0
    anf = ""
    if (v[0] == 1):
        anf +="1"
    for i in range(len(v)):
        if (v[i] == 1):
            flag += 1
            # 第一次不加+
            if (flag > 1):
                anf += " + "
            a = bin(i)[2:]
            temp, count = 0, 0      
            for j in range(len(a)-1,-1,-1):
                temp += 1
                if (a[j] == '1' and temp != 0):
                    anf +="x"+str(temp-1)
                    count +=1
                if (temp == 0):
                    anf += "1"
                if (count > degree):
                    degree = count
    return (anf, degree)

def nonliearity_bf(v):
    """返回布尔函数的非线性度int
    para: v 真值表
    """
    n = get_n(v)
    abs_wht = list(map(abs,fwt(v)))
    nonliearity = (2**(n-1))-max(abs_wht)/2
    # 公式 dH = 2^(n-1) - max|Sf(w)|/2 
    
    return nonliearity

def is_bf_bent(v):
    """返回布尔函数是否为bent"""
    n = get_n(v)
    if n % 2 != 0:
        return False
    elif nonliearity_bf(v) == (2**(n-1)) * (1-2**((-1)*(n/2))):
        return True

def is_bf_balanced(v):
    """返回布尔函数是否为平衡"""
    if v.count(1)!=v.count(0):
            return False
    return True

def is_bf_rotation_symmetric(v):
    """
    返回布尔函数是否为旋转对称函数
    一个布尔函数称为旋转对称的当且仅当对其输入向量进行循环移位时, 输出值保值不变"""
    #todo: 再看一卡
    n = get_n(v)
    flag = True
    num = []
    for i in range(n+1):
        num.append(2**i-1)
    for i in num:
        num = binary(i, n)
        temp = v[i]
        for j in range(1,n,1):
            x = num[-j:]+num[:-j]
            if v[int(x,2)] == temp:
                pass
            else:
                flag=False
                return flag
    return flag

def derivative(v,u):
    """
    Return the derivative in direction of u
    sage: u – either an integer or a tuple/list of F2 elements of length equal to the number of variables
    #todo:
    """
    res = []
    for i in range(len(v)):
        tmp = v[i^u] ^ v[i]
        res.append(tmp)
    return res 

def autocorrelation(v):
    """返回布尔函数关于a 的自相关因数autocorrelation coefficient"""
    #todo 增加默认返回全部，如果设置参数了返回特定的
    res = []
    for a in range(len(v)):
        sum = 0
        for x in range(len(v)):
            if ((v[x ^ a] ^ v[x]) == 0):
                sum += 1		
            else:
                sum -= 1	
        res.append(sum)
    return res

def has_bf_linear_structure(v):
    """Return True if this function has a linear structure.
    An n-variable Boolean function f has a linear structure 
    if there exists a nonzero a∈Fn2 such that f(x⊕a)⊕f(x) is a constant function."""
    flag = 1
    for a in range(1, len(v)):
        cons = v[0] ^ v[a]
        for x in range(1, len(v)):
            tmp = v[x] ^ v[x^a]
            if cons != tmp:
                flag = 0
        if (x== len(v)-1) & (flag == 1):
            return True
    return False

def main():
    v = [0,1,0,0,0,1,1,1]
    n = int(math.log(len(v), 2))
    x = (2**(n-1)) * (1-2**((-1)*(n/2)))
    print(is_bf_rotation_symmetric(v,n))

if __name__ == "__main__":
    main()