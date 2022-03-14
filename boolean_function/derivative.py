#
from ANF import ANF

def derivative(v,u):
    """
    Return the derivative in direction of u
    para: v - bf真值表, u - direction
    The derivative of f in direction of u is defined as x↦f(x)+f(x+u).
    sage: u – either an integer or a tuple/list of F2 elements of length equal to the number of variables
    #! 这里增加tuple/list
    """
    res = []
    for i in range(len(v)):
        tmp = v[i^u] ^ v[i]
        res.append(tmp)
    return res 

def main():
    S=[3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    # v = [0,1,0,1,0,1,0,1]
    v = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0]

    u = 4
    derivative_func = derivative(v,u)
    print(ANF(derivative_func)[0])


if __name__ == "__main__":
    main()

