import math

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

def ANF(v):             
    """函数返回布尔函数的字符串格式代数标准形式和代数次数deg f
    param: v - 布尔函数的真值表
    e.g. : v = [0,1,0,0,0,1,1,1]
    """
    n = int(math.log(len(v),2))
    
    # for i in range(n):
    #     t = []
    #     u = []
    #     for j in range(2 ** (n - 1)):
    #         t.append(v[2 * j])
    #         u.append(v[2 * j + 1] ^ v[2 * j])
    #     v = t + u
    # print("V:\t" ,v)

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

def nonliearity_bf(v, n):
    """返回布尔函数的非线性度int
    para: v 真值表
          n n元布尔函数
    """
    
    abs_wht = list(map(abs,fwt(v)))
    nonliearity = (2**(n-1))-max(abs_wht)/2
    # 公式 dH = 2^(n-1) - max|Sf(w)|/2 
    
    return nonliearity

def is_bent(v, n):
    if n % 2 != 0:
        return False
    
    elif nonliearity_bf(v) == (2**(n-1)) * (1-2**((-1)*(n/2))):
        return True

def is_balanced(v):
    """返回布尔函数是否为平衡"""
    if v.count(1)!=v.count(0):
            return False
    return True

def main():
    v = [0,1,0,0,0,1,1,1]
    n = 4
    x = (2**(n-1)) * (1-2**((-1)*(n/2)))
    print(x)

if __name__ == "__main__":
    main()