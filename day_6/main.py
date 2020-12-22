t = int(input())
for i in range(t):
    s = input()
    odd_order = ""
    even_order = ""
    for order in range(len(s)):
        if (order + 1) % 2 == 1:
            odd_order = odd_order+s[order]

        elif (order + 1) % 2 == 0:
            even_order = even_order+s[order]

    print(odd_order+" "+even_order)
