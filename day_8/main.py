n = int(input())
phoneBooks = {}
for i in range(n):
    i_val = input().split(" ")
    phoneBooks[i_val[0]] = i_val[1] 


for i in range(n):
    check_string = input()
    if check_string in phoneBooks:
        print(check_string + "=" + phoneBooks[check_string])
    else:
        print("Not found")