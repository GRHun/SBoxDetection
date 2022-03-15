from get_size import get_size
from get_all_bflc import get_all_bflc
from boolean_function import has_bf_linear_structure

def has_linear_structure(S,N,M):
    """是否有线性结构"""
    bflc = get_all_bflc(S,N,M)
    for i in bflc:
        if has_bf_linear_structure(i) ==True:
            return True
    return False


def main():
    # S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12] 
    S=[12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]
    N, M = get_size(S)
    print(has_linear_structure(S,N,M))


if __name__ == "__main__":
    main()

