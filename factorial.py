def fact(number):
    result=1
    for i in range(1,number+1):
        result=result*i
    return result
print(fact(5))
