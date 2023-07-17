def search(num, arr):
    arr = [i for i in arr]

    middle = (len(arr) // 2) -1
    if num == arr[middle]:
        return True
    elif len(arr) <= 1:
        return False
    elif num > arr[middle]:
        return search(num, arr[middle+1:])
    elif num < arr[middle]:
        return search(num, arr[:middle])

def sort(arr):
    nums = [i for i in arr]

    for i in range(len(nums)):
        swaped = 0
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swaped += 1
        if swaped == 0:
            break
    return nums

def bSearch(num, arr):
    arr = sort([i for i in arr])
    return search(num, arr)
