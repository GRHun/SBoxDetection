from boolean_function import has_bf_linear_structure
from get_all_bflc import get_all_bflc
from get_size import get_size


def name(S,N,M,index):       
    """
    返回所选择的S盒特定组成函数的线性组合 
    in: x0+x1+x2
    out:真值表， num    
    """
    size = len(S)
    print("===>1. ",index)
    # M = int(math.log(size, 2))
    # N = len(bin(max(S)).lstrip("0b"))
    n = 2 ** M
    temp = index.lower().split("+")
    print("===>2. ", temp)
    choose = []
    for i in temp:
        choose.append(int(i.lstrip('x')))
    print("===>3. ", choose)
    
    num = 0
    for i in choose:
        num += 2**i
        print("====>num: ",num)
    
    booleanfunc = []
    for j in range(size):
        if(bin(num&S[j]).count("1")) % 2 ==0:
            booleanfunc.append(0)
        else:
            booleanfunc.append(1)
    return (booleanfunc,num)

"""
        if(num>=len(sbox)):
            msg = QMessageBox()
            msg.setWindowTitle("Failed")
            msg.setText("请确定选择的函数正确，在该S盒组成布尔函数的线性组合集合中")
            x = msg.exec()
"""


def main():
    # S = [3,8,15,1,10,6,5,11,14,13,4,2,7,0,9,12]
    S = [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0]
    N, M = get_size(S)
    # print(name(S,N,M,'x2'))
    print(name(S,N,M,"x0+x3"))


    

if __name__ == "__main__":
    main()