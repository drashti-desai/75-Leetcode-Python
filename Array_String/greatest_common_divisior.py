
#function: it finds greatest common divisior of 2 strings using 'string divisibility'
def gcd_of_strings(str1: str, str2: str) -> str:
    len1, len2 = len(str1), len(str2)

    def isDivisior(l):
        if len1 % l or len2 % l:
            return False
        
        f1, f2 = len1 // l, len2 // l
        return str1[:l] * f1 == str1 and str2[:l] * f2 == str2

    for l in range(min(len1, len2), 0, -1):
        if isDivisior(l):
            return str1[:l]

    return "No common divisor"

# add user input
if __name__ == "__main__":
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # call the function and display result
    result = gcd_of_strings(str1, str2)
    print(f"GCD of String: {result}")