def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

resul = sum_with_range(1,10)
print(resul)
resul_2 = sum_with_range(resul,resul+10)
print(resul_2)