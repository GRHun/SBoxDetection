from nonlinearity_bf import nonliearity_bf

def is_bent(v, n):
    if n % 2 != 0:
        return False
    
    elif nonliearity_bf(v) == (2**(n-1)) * (1-2**((-1)*(n/2))):
        return True

def main():
    v = [0,1,0,0,0,1,1,1]
    n = 3
    print("is_bent: ",is_bent(v, n))


if __name__ == "__main__":
    main()