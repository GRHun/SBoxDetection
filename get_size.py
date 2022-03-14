import math

def get_size(S):
    """返回nxm的S盒的输入N，输出M
    """
    size = len(S)
    N = int(math.log(size, 2))
    M = len(bin(max(S)).lstrip("0b"))

    return N, M

def main():
    S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    print(get_size(S))


if __name__ == "__main__":
    main()

