import math

def generate_primes(amt_of_numbers):
    prime_nums_list = []
    for i in range(2, amt_of_numbers):
        for j in range (2, i):
            if (i % j) ==0:
                break
        else:
            prime_nums_list.append(i)
    return prime_nums_list


if __name__ == '__main__':
    amt_of_numbers = input("Enter the range of prime numbers you wish to generate: ")
    print('\n')
    print("Okay, printing prime numbers between 0 and " + amt_of_numbers + "...")
    prime_nums_list = generate_primes(int(amt_of_numbers))
    #prime_nums_list.append(2)
    prime_nums_list.sort()

    count = 1
    
    print(prime_nums_list)
        #print('\n')

    #print (count)



