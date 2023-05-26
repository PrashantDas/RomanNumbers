# Program to convert Arabic numbers to Roman numbers


# maps powers to the respective characters for numbers formed by 1
book_1 = {0: 'I',
          1: 'X',
          2: 'C',
          3: 'M'}

# maps powers to the respective characters for numbers formed by 5
book_5 = {0: 'V',
          1: 'L',
          2: 'D'}


def style(n, power):
    """takes in a digit and its place value as a power of 10 and uses the
    characer power mapping and placement style of roman characters in a number
    to generate the given roman number"""
    if n == 1:
        answer = book_1[power]*1
    elif n == 2:
        answer = book_1[power]*2
    elif n == 3:
        answer = book_1[power] * 3
    elif n == 4:
        answer = book_1[power] + book_5[power]
    elif n == 5:
        answer = book_5[power]
    elif n == 6:
        answer = book_5[power] + book_1[power]
    elif n == 7:
        answer = book_5[power] + book_1[power] + book_1[power]
    elif n == 8:
        answer = book_5[power] + book_1[power] + book_1[power] + book_1[power]
    elif n == 9:
        answer = book_1[power] + book_1[power+1]
    else:
        answer = ''
    return answer


def digits_powers(n):
    """makes a list of tuples with powers as the first item
    and digits as the second item of the tuples"""
    power = -1
    dp = dict()
    while n != 0:
        digit = n % 10
        dp[power+1] = digit
        n //= 10
        power += 1
    return sorted(dp.items(), reverse=True)



def starter(num: int)-> str:
    try:
        int(num)
        num = int(num)
        if num > 3999:
            output = "Number is too large to process"
        elif num < 1:
            output = "The Romans didn't have zero. Enter a bigger number."
        else:
            result = ''
            for each in digits_powers(num):
                power = each[0]
                digit = each[1]
                result += style(digit, power)
            output = result
        return output
    except:
        return "Enter only digits"



# I have prior knowledge of Roman numerals, and can represent any Arabic number below 4000 in it's Roman form.


