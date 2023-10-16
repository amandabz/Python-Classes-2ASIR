def confirm_odd_even_number():
    
    num = int(input("Enter a number: "))

    if (num % 2) == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))


confirm_odd_even_number()
