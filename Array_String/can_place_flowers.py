from typing import List

# function: check each place of list w
def can_place_lowers(flowerbed: List[int], n: int) -> bool:
    f = [0] + flowerbed + [0]

    # 1st solution
    # count = 0

    #  for i in range(1, len(f) - 1):

    #     if f[i-1:i+2] == [0, 0, 0]:

    #         f[i] = 1
    #         count += 1

    #     if count >= n:
    #         return True

    #  return False
    
    # 2nd solution
    # skip first & last
    for i in range(1, len(f) - 1): 
        if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
            f[i] = 1
            n -= 1
    return n <= 0

if __name__ == "__main__":
    flowerbed_input = input("Enter the flowerbed (comma-separated 0s and 1s): ")
    n = int(input("Enter the number of flowers to place: "))   

    # Convert the input string to a list of integers
    flowerbed = list(map(int, flowerbed_input.split(',')))

    # Call the function and print the result
    result = can_place_lowers(flowerbed, n)
    print(f"Can place {n} flowers: {result}")
         