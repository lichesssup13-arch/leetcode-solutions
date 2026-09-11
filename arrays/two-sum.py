def two_sum(nums, target):
    i = 0
    j = i+1
    while True:
        if nums[i] + nums[j] == target:
            break
        elif j == len(nums) - 1:
            if i == j - 1:
                return [ -1, -1]
            i +=1
            j = i +1
        else:
            j +=1
    return [i, j]

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # Ожидается [0, 1]
    print(two_sum([3, 2, 4], 6))       # Ожидается [1, 2]
    print(two_sum([3, 3], 6))          # Ожидается [0, 1]