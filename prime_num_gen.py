import math

def prime_over_40(num):
    prime = num^2 + num + 41
    return prime

def prime_plus_one(num):
    prime = 6 * num + 1
    return prime

def prime_minus_one(num):
    prime = 6 * num -1
    return prime

def generation_loop(amt_to_gen):
    prime_nums_list = []
    for i in range(amt_to_gen):
        if(i <= 40 ):
            num1 = (prime_minus_one(i))
            num2 = (prime_plus_one(i))
            if num1 not in prime_nums_list:
                prime_nums_list.append(num1)
            
            if num2 not in prime_nums_list:
                prime_nums_list.append(num2)
        else:
            num1 = (prime_over_40(i))
            if num1 not in prime_nums_list:
                prime_nums_list.append(num1)

        
    return prime_nums_list   


if __name__ == '__main__':
    amt_of_numbers = input("Enter the amount of prime numbers you wish to generate: ")
    print('\n')
    print("Okay, printing " + amt_of_numbers + " numbers...")
    prime_nums_list = generation_loop(int(amt_of_numbers))
    prime_nums_list.append(2)
    prime_nums_list.append(3)
    prime_nums_list.sort()

    count = 1
    for i in range(2, int(amt_of_numbers)+1):
        print(prime_nums_list[i])
        count +=1
        #print('\n')

    print (count)



