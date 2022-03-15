

def has_linear_structure(v):
    """Return True if this function has a linear structure.
    An n-variable Boolean function f has a linear structure 
    if there exists a nonzero a∈Fn2 such that f(x⊕a)⊕f(x) is a constant function."""
    flag = 1
    for a in range(1, len(v)):
        cons = v[0] ^ v[a]
        for x in range(1, len(v)):
            tmp = v[x] ^ v[x^a]
            if cons != tmp:
                flag = 0
        if (x== len(v)-1) & (flag == 1):
            return True
    return False 

                
def main():
    # S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    # N, M = get_size(S)
    v1 = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0]
    # v2 = [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
    v3 = [1, 0, 1, 0, 0, 1, 0, 0]


    print(has_linear_structure(v1))
    print(has_linear_structure(v3))


if __name__ == "__main__":
    main()

