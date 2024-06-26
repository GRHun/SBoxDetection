from boolean_function import is_bf_balanced
from get_all_bflc import get_all_bflc
#
from get_size import get_size


def is_balanced(S, N, M):
    bflc = get_all_bflc(S,N,M)
    flag = True
    for i in bflc:
        if not is_bf_balanced(i):
            flag = False
    return flag


def main():
    S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    N, M = get_size(S)
    print(is_balanced(S,N,M))


if __name__ == "__main__":
    main()