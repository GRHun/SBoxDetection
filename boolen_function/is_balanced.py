def is_balanced(v):

    if v.count(1)!=v.count(0):
            return False
    return True

def main():
    v = [0,1,0,0,0,1,1,1]
    n = 4
    print(is_balanced(v))

if __name__ == "__main__":
    main()