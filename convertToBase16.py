import sys

def convertToBase(num, base):
    temp = int(num)
    base = int(base)
    if temp == 0:
        return "0"

    digits = "0123456789ABCDEF"  # for bases up to 16
    result = []

    while temp > 0:
        print(f"{temp}/{base} = {temp//base}")  
        print(f"Remainder is {temp%base}")
        remainder = temp % base
        result.append(digits[remainder])
        temp = temp // base

    # reverse the result to get the correct order
    result.reverse()
    return "".join(result)

# Example usage:
if len(sys.argv) == 3:
    print(convertToBase(sys.argv[1], sys.argv[2]))
else:
    print("Usage: python script.py <number> <base>")