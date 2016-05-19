string_number_dict = {
    0 : "",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"}

def one_digit(n):
    return len(string_number_dict[n])

def two_digits(n):
    tens, remainder = divmod(n, 10)
    return len(string_number_dict[tens * 10]) + one_digit(remainder)

def three_digits(n):
    hundred = len('hundred')
    a = len('and')

    hundreds, remainder = divmod(n,100)
    if remainder == 0:
        a = 0
        rest = 0
    elif remainder < 10:
        rest = one_digit(remainder)
    elif remainder < 20:
        rest = len(string_number_dict[remainder])
    else:
        rest = two_digits(remainder)
    
    return len(string_number_dict[hundreds]) + hundred + a + rest

def four_digits(n):
    thousand = len('thousand')

    thousands, remainder = divmod(n, 1000)
    return len(string_number_dict[thousands]) + thousand + len(string_number_dict[remainder])

def main():
    result = 0

    for num in range(1, 1001):
        print(num)
        if num < 10:
            print(one_digit(num))
            result += one_digit(num)
        elif num < 20:
            print(len(string_number_dict[num]))
            result += len(string_number_dict[num])
        elif num < 100:
            print(two_digits(num))
            result += two_digits(num)
        elif num < 1000:
            print(three_digits(num))
            result += three_digits(num)
        else:
            print(four_digits(num))
            result += four_digits(num)
    return result

if __name__ == "__main__":
    print(main())
