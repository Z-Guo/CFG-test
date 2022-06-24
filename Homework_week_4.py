# """
# Question 1
# """
#
# return true when pin code matches, if not, show input. If is a match -> True, if not -> input again.



def pin_validation(pin_input):
    correct_pin = 1103
    if pin_input == correct_pin:
        return True
    else:
        return pin_attemps()

def withdrawal_validation(withdrawal):
    balance = 100
    if withdrawal > balance:
        raise Exception("withdrawal amount cannot be higher than your balance ")
    if withdrawal < 0:
        raise ValueError("Incorrect input: withdrawal cannot be negative")

def pin_attemps():
    correct_pin = 1103
    attemps = 0
    while attemps < 3:
        another_input = int(input('re-enter?'))
        attemps += 1
        if correct_pin == another_input:
            return
        if correct_pin != another_input and attemps == 3:
            raise Exception("you have tried too many times")

def calculate_new_balance(withdrawal):
    balance = 100
    new_balance = balance - withdrawal
    return new_balance

def pin_digits_validation(user_input_pin_code):
    if len(str(user_input_pin_code)) < 4 or len(str(user_input_pin_code)) > 4 :
        raise ValueError("Incorrect input: your pin code must be 4 digits")

isSuccessful = False
#
# try:
#     user_input_pin_code = int(input('What is your pin code?'))
#     pin_digits_validation(user_input_pin_code)
#     pin_validation(user_input_pin_code)
#     withdrawal = int(input('How much would you like to withdrawal?'))
#     withdrawal_validation(withdrawal)
#     calculate_new_balance(withdrawal)
#
# except ValueError as exc:
#     print("Invalid input %s" % exc)
#
# else:
#     isSuccessful = True
#     print(f'you have successfully withdrawal £{withdrawal}')
#
