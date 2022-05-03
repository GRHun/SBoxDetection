# out_T = [[0 for i in range(2**n)] for j in range(2**n)]

# def create_lis(n):
#     a= [[] for i in range(2**n)]
#     return a
bct1 = []
for out in range(2**n):
    # T = create_lis(n)
    T = [[] for i in range(2**n)]
    for x in range(2**n):
        left  = x ^ (s.index(s[x]^out))
        T[left].append(x)

    need = []
    col = [0 for i in range(2**n)]
    for ele in T:
        if len(ele) != 0:
            need.append(ele)

    for ele in need:
        for i in range(len(ele)):
            for j in range(len(ele)):
                tmp = ele[i]^ele[j]
                col[tmp] += 1
    bct1.append(col)

bct = list(map(list,zip(*bct1)))

for i in bct:
    print(i)

