def reverse_vowels(self, s: str) -> str:
        s = list(s)
        # print(s)
        vowels = set('aeiouAEIOU')

        i, j = 0, len(s)-1

        while(i<j):
            if(s[i] not in vowels):
                i += 1
            elif(s[j] not in vowels):
                j -= 1
            else:
                 s[i], s[j] = s[j], s[i]
                 i += 1
                 j -= 1
                
        return "".join(s)

if __name__ == "__main__":
    flowerbed_input = input("Enter the flowerbed (comma-separated 0s and 1s): ")
    n = int(input("Enter the number of flowers to place: "))   

    # Convert the input string to a list of integers
    flowerbed = list(map(int, flowerbed_input.split(',')))

    # Call the function and print the result
    result = reverse_vowels(flowerbed, n)
    print(f"Can place {n} flowers: {result}")