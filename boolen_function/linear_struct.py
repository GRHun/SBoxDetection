def if_ls_def(n, v, s):
    result = -1
    if v[s] == 0:
        result =1
    elif v[s] == 1:
        result =0
    else:
        return False
    for i in range(1, 1<<n):
        # python 没有 case 我是没想到的
        #print(i, f[i], f[i^s])
        if v[i]^v[i^s]^result:
            pass
        else:
            return False
    return True


def print_liner_structure(v, n):
    res = False
    for s in range(1, 1<<n):
        if if_ls_def(n, v, s):
            if not res:
                res = True
            print(bin(s)[2:])
    return res