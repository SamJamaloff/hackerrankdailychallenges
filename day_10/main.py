if __name__ == '__main__':
    # n = int(input())
    n = 125
    cc_one = 0
    mc_one = 0
    while n > 0:
        r = n % 2
        if r == 1:
            cc_one +=1
            if cc_one > mc_one:
                mc_one = cc_one
        else: 
            cc_one = 0
        n = n // 2

    print(mc_one)