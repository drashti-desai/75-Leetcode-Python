
# function: arrange two string alternatively
def merge_alternately(word1: str, word2: str) -> str:
    res = []

    i,j = 0,0
    while(i < len(word1)) and (j < len(word2)):
        res.append(word1[i])
        res.append(word2[j])
        i += 1
        j += 1

    res.append(word1[i:])
    res.append(word2[j:])

    return "".join(res)

# add user input
if __name__ == "__main__":
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    # call the function and display result
    result = merge_alternately(word1, word2)
    print(f"Merged result: {result}")