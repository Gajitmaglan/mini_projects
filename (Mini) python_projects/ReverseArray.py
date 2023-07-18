while True:
    print("Note: type 'exit' or 0 to exit.")
    inputted = input("input array length: ")

    if inputted == 'exit':
        break

    try:
        arr_length = int(inputted)
        if arr_length == 0:
            break
    except ValueError:
        print("Invalid input.")
        continue

    nums = list(range(arr_length))
    print(nums)

    size = len(nums)
    hiindex = size - 1
    mid = size//2

    for i in range(mid):
        temp = nums[hiindex]
        nums[hiindex] = nums[i]
        nums[i] = temp
        hiindex -= 1

    print(nums)
