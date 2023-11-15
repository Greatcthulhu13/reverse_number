def reverse_number(num):
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return reversed_num

number = int(input("Enter a number: "))

result = reverse_number(number)
print(f"The reverse of {number} is: {result}")
