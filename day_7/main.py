if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    reversed_arr = [i for i in reversed(arr)]
    print(reversed_arr)
    
    print_string = ""
    for i in reversed_arr:
        print_string +=(str(i)+" ")
    print(print_string)