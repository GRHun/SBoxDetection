from get_size import get_size

def get_all_bflc(S, N, M):         
    """返回S盒坐标函数的所有非零线性组合
    """
    n = 2 ** M
    result=[]
    # todo: 就是说可以在直接用size吗？为啥设置一个n
    for i in range(1,n):
        booleanfunc_a = []
        for j in range(len(S)):
            # todo: 看到报告里伪代码是1，修改了，不知是否有影响
            if(bin(i&S[j]).count("1")) % 2 ==1:
                booleanfunc_a.append(0)
            else:
                booleanfunc_a.append(1)
        result.append(booleanfunc_a)
    return result


def main():
    S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    # print(len(S))
    N, M = get_size(S)
    a = get_all_bflc(S)


if __name__ == "__main__":
    main()



