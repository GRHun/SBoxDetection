import math

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
        for i in range(2**(n-k)):  
            # Compute the image of the i-th 2k-bit block
            for j in range((2**(k-1))):
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


def main(ANF):
    #truth table
    v1 = [0,1,0,0,0,1,1,1]
    v2 = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0]
    v3 =[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0]
    (anf,degree)=ANF(v1)
    print("[+]==>\t真值表1：",v1)
    print("\tANF\t",anf,"\n\tdegree:\t",degree)

    (anf,degree)=ANF(v2)
    print("[+]==>\t真值表2：",v2)
    print("\tANF\t",anf,"\n\tdegree:\t",degree)

    (anf,degree)=ANF(v3)
    print("[+]==>\t真值表3：",v3)
    print("\tANF:\t",anf,"\n\tdegree:\t",degree)




    """
    in:     v = [0,1,0,0,0,1,1,1]    
    
    out:    ANF      x0 + x0x1 + x1x2
            degree   2
    """

if __name__ == "__main__":
    main(ANF)