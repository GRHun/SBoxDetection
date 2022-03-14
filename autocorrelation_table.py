from get_size import get_size

def autocorrelation_table(S,N,M):
    AUT = [[0 for i in range(2**M)] for j in range(2**N)]
    
    

def main():
    S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    N, M = get_size(S)
    autocorrelation_table()


if __name__ == "__main__":
    main()

