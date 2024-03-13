import imp
from ANF import ANF
from get_all_bflc import get_all_bflc
from get_size import get_size

#! 是返回什么的代数系数呢？

def get_max_degree(S):
    pass

    

def main():
    
    S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    N,M= get_size(S)
    print(get_max_degree(S))


if __name__ == "__main__":
    main()

