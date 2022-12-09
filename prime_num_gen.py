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
        if(i <= 40):
            prime_nums_list.append(prime_minus_one(i))
            prime_nums_list.append(prime_plus_one(i))
        else:
            prime_nums_list.append(prime_over_40(i))
        
    return prime_nums_list   


if __name__ == '__main__':
    amt_of_numbers = input("Enter the amount of prime numbers you wish to generate: ")
    print('\n')
    print("Okay, printing " + amt_of_numbers + " numbers...")
    prime_nums_list = generation_loop(int(amt_of_numbers))

    count = 1
    for i in range(1, int(amt_of_numbers)):
        print(prime_nums_list[i])
        count +=1
        #print('\n')

    print (count)



