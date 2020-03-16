# Ask to input the interger
user_number = int(input ("Input your number pls: "))

if user_number > 1:
    for i in range(2, user_number):
        if (user_number % i) == 0:
            print(user_number, "is not a prime number")
            break
    else:
        print("true", user_number, "is a prime number")

else:
    print("False", user_number, "is not a prime number")