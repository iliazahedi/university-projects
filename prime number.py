adad = int(input("Enter a number: "))

if adad <= 1:
    print("It is not a prime number!!")
else:
    is_prime = True
for i in range(2, adad):
    if adad % i == 0:
        is_prime = False
        break
if is_prime:
    print("It is a prime number!!")
else:
    print("It is not a prime number!")
