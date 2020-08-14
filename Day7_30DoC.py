n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

c = ""
for x in arr[::-1]:
    c += str(x) + " "
print(c)