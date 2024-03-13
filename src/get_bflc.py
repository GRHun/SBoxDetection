import math

def get_bflc(S,string):         
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

def main():
    s=[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0]
    
    # print("".join(list(map(str,get_bflc(s,"x3")))))
    print(get_bflc(s,"x2"))
    # print(get_bflc(s,"x1"))
    # print(get_bflc(s,"x0"))
    # print(get_bflc(s,"x0+x3"))


if __name__ == "__main__":
    main()