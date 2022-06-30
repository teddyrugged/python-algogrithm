'''Validation of a debit card and credit card '''

def digits_of(n):
        return [int(d) for d in str(n)]

def card_validator(card_number):
    if card_number == None:
        card_number = input("Enter credit card number: ")
    try:
        card_digits = digits_of(card_number)
    except Exception:
        return "INVALID"
    odd_digits = card_digits[-1::-2]
    even_digits = card_digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    if checksum % 10 == 0:
        card_number = str(card_number) 
        if len(card_digits) == 15 and int(card_number[0:2]) in [34,37]:
            return "AMEX"
        elif len(card_digits) == 16 and int(card_number[0:2]) in range(51,56):
            return "MASTERCARD"
        elif len(card_digits) == 13 or len(card_digits) == 16 and int(card_number[0]) == 4:
            return "VISA"
    return "INVALID"
print(card_validator(23566456654334))




# American Express

# 378282246310005

# American Express

# 371449635398431

# American Express Corporate

# 378734493671000

# Australian BankCard

# 5610591081018250

# Diners Club

# 30569309025904

# Diners Club

# 38520000023237

# Discover

# 6011111111111117

# Discover

# 6011000990139424

# JCB

# 3530111333300000

# JCB

# 3566002020360505

# MasterCard

# 5555555555554444

# MasterCard

# 5105105105105100

# Visa

# 4111111111111111

# Visa

# 4012888888881881

# Visa

# 4222222222222
