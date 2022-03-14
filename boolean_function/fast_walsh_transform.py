# todo: 选择其中一个方法，然后看下复杂度


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



def main():
    v = [0,1,0,0,0,1,1,1]
    wht = fwt(v)
    print("wht: ",wht)


if __name__ == "__main__":
    main()