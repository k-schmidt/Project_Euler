def factorial(num):
    multi = 1

    for n in range(2, num+1):
        multi *= n
    return multi

def sum_digits_from_num(num):
    sum_of_digits = 0
    num_to_str = lambda x: str(x)
    str_num = num_to_str(num)
    
    for s in str_num:
        sum_of_digits += int(s)
    return sum_of_digits

if __name__ == "__main__":
    fact = factorial(100)
    print(sum_digits_from_num(fact))