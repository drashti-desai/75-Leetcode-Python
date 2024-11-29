#  function: by comparing total number of candies with maximum one while ietration
from typing import List


def kids_with_candies(candies: List[int], extraCandies: int) -> List[bool]:
        result = []

        for i in range(len(candies)):
            if candies[i]+extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)

        return result

# add user input and display output
if __name__ == "__main__":
    # input the list of candies
    candies = list(map(int, input("Enter the number of candies for each kid (space-separated): ").split()))
    # input the number of extra candies
    extraCandies = int(input("Enter the number of extra candies: "))

    # call the function and display the result
    result = kids_with_candies(candies, extraCandies)
    print(f"Result: {result}")