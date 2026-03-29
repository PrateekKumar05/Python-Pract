def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[0:length - 1]  # Fix off-by-one error here
    given_check_digit = isbn[length - 1]  # Fix off-by-one error here

    # Convert main digits to int list, handle invalid chars
    main_digits_list = []
    for digit in main_digits:
        if not digit.isdigit():
            print("Invalid character was found.")
            return
        main_digits_list.append(int(digit))

    # Calculate expected check digit
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # For ISBN-10, the given check digit can be 'X' or digit
    # For ISBN-13, it's always digit
    # So compare them as strings (upper case for 'X')
    if given_check_digit.upper() == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - digits_sum % 11
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    result = 10 - digits_sum % 10
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    try:
        user_input = input('Enter ISBN and length: ')
        values = user_input.split(',')
        if len(values) != 2:
            print("Enter comma-separated values.")
            return

        isbn = values[0]
        length_str = values[1].strip()

        if not length_str.isdigit():
            print("Length must be a number.")
            return
        length = int(length_str)

        if length not in (10, 13):
            print('Length should be 10 or 13.')
            return

        validate_isbn(isbn, length)

    except IndexError:
        print("Enter comma-separated values.")
    except ValueError:
        print("Invalid character was found.")
    except Exception as e:
        # Catch-all for unexpected exceptions
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()