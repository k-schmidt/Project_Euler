import operator

def is_even(number):
    if number % 2 == 0:
        return True

def generate_collatz(max_number):
    max_dict = dict()

    for n in range(2, max_number + 1):
        max_dict[n] = 0
        i = n

        while i != 1:
            if is_even(i):
                i = i // 2
            else:
                i = (3 * i) + 1
            if i in max_dict:
                max_dict[n] += max_dict[i]
                break
            max_dict[n] += 1
    return max_dict

def get_key_for_max_value(collatz_dict):
    return max(collatz_dict.items(), key=operator.itemgetter(1))[0]

def main(max_number=1000000):
    collatz_dict = generate_collatz(max_number)
    max_key = get_key_for_max_value(collatz_dict)
    return max_key

if __name__ == '__main__':
    print(main())
