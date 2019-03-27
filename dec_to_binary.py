def dec_to_binary(number):
    result = ""
    if number == 0:
        return 0
    else:
        while number >=1:
            result = str((number % 2))+result
            number = number // 2
        return result

print(dec_to_binary(1))
print(dec_to_binary(0))
print(dec_to_binary(8))
print(dec_to_binary(13))
