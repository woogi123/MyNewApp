a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = []
for i in a:
    if i % 2 == 0:
        result.append(i**2)
    else:
        result.append(i)
        
        
print(result)