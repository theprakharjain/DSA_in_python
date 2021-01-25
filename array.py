arr = [33,45,66,48]

# print(arr)
# print(arr[2])
# print(arr[0:2])
# print(arr[1:3])
# print(arr[:3])
# print(arr[:-1])
# print(arr[:])

# arr[2] = 18
# print(arr)


def find_max_in_array(arr):
    max = 0

    for num in arr:
        if num > max:
            max = num

    print("Maximum number is: " + str(max))

find_max_in_array(arr)
