from fast_walsh_transform import fwt

def nonliearity_bf(v, n):
    """返回布尔函数的非线性度int
    para: v 真值表
          n n元布尔函数
    """
    
    abs_wht = list(map(abs,fwt(v)))
    nonliearity = (2**(n-1))-max(abs_wht)/2
    # 公式 dH = 2^(n-1) - max|Sf(w)|/2 
    
    return nonliearity

def main():
    v = [0,1,0,0,0,1,1,1]
    print("非线性度：", nonliearity_bf(v,3))


if __name__ == "__main__":
    main()