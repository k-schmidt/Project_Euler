def compute_exponent_base_two(exp):
    return 2 ** exp

def int_to_string(integer):
    return str(integer)

def main(exp):
    exponent = compute_exponent_base_two(exp)
    string_int = int_to_string(exponent)
    result = 0
    for i in string_int:
        result += int(i)
    return result

if __name__ == "__main__":
    print(main(1000))
