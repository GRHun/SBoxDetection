import math


# ! 找个例子验证以下
def is_bf_perfect_nonlinear(v):
    n = int(math.log(len(v), 2))
    tmp1, tmp2 = 0, 0
    for a in range(1, n):
        for x in range(0, n):
            if v[x] ^ v[x^a] == 0:
                tmp1 += 1
            elif v[x] ^ v[x^a] == 1:
                tmp2 += 1
    if (tmp1 == 2**(n-1)) & (tmp2 ==2**(n-1)):
        return True
    return False

    

def main():
    v1 = [0,1,0,0,0,1,1,1]
    v2 = [0, 1, 1, 0, 1, 0, 1, 0]

    print(is_bf_perfect_nonlinear(v2))

if __name__ == "__main__":
    main()
