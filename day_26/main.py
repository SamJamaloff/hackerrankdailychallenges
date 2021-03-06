# Enter your code here. Read input from STDIN. Print output to STDOUT
# list comprehension https://docs.python.org/3/tutorial/datastructures.html
return_day, return_month, return_year = [int(e) for e in input().strip().split(' ')]
due_day, due_month, due_year = [int(e) for e in input().strip().split(' ')]

# need to check for biggest category first
if return_year < due_year:
    print(0)
elif return_year == due_year:
    # Check for the month    
    if return_month < due_month:
        print(0)
    elif return_month == due_month:
        #Check for the day
        if return_day <= due_day:
            print(0)
        else:
            print(15*(return_day - due_day))
    else:
        print(500*(return_month - due_month))  
else:
    print(10000)
