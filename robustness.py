def robustness(table,diffuniformity,N):
    """
    返回S盒的鲁棒性
    𝜂(𝑆) = (1 − 𝜎(𝑆)/2𝑛)(1 − 𝛿(𝑆)/2𝑛)
    要使差分分布表的第一列包含尽可能少的非零元素
    """
    sum = 0
    for i in table:
        if(i[0] == 0):
            sum += 0
        else:
            sum += 1
    result = (1-sum/(2**N))*(1-diffuniformity/(2**N))
    return result
