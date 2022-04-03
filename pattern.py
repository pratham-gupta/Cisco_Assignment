try:
    n = int(input("please provide height of tree."))
except:
    print('Invalid input, using default value 4')
    n = 4

last_element = 1
for i in range(1,n+1):
    curr_list = range(last_element, last_element+i)
    print(*curr_list[::-1],sep=" ")
    last_element = curr_list[-1]+1
