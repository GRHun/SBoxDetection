
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


def main():
    # S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    # N, M = get_size(S)
    # v = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0]
    # v = [1, 1, 0, 0, 0, 0, 0, 0]
    v = (0, 1, 0, 0, 1, 0, 0, 0) 
    
    print(autocorrelation(v))



if __name__ == "__main__":
    main()