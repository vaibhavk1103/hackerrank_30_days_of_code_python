n = int(input().strip())
num = list((bin(n).split('b'))[1])
num.insert(0, '0')
num.append('0')
count = 0
store = 0
for i in range(0, len(num)):
    if (num[i]) == '1':
        count += 1
    elif ('0' == (num[i])) and count != 0:
        if count >= store:
            store = count
        count = 0
print(store)