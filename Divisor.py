def divisor(num):
    divisor_list = [1]
    for i in range(2, num+1):
        if num % i == 0:
            divisor_list.append(i)
    return divisor_list

num = int(input('input number : '))
print('divisors : ', end='')
print(divisor(num))