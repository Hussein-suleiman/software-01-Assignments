def remove_odds(numbers):
    return [n for n in numbers if n % 2 == 0]

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    evens = remove_odds(nums)
    print("Original list:", nums)
    print("Even numbers only:", evens)

main()
