while True:
    name = input("My name is (note: type 'exit' to exit): ")
    if (name == 'exit'):
        break
    arr = list(name)

    print("ASCII for each letter: ", end="")
    ascii_values = []
    for character in name:
        ascii_values.append(ord(character))
    print(ascii_values)

    """ Bubble Sort Algorithm: """
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    print("My bubbleSorted name is ", end = "")
    for i in range(len(arr)):
        print(arr[i], end = "")

    print('')

    SortedName = ''.join(arr)

    print("BubbleSorted ASCII is: ", end = "")
    SortedASCII = []
    for element in SortedName:
        SortedASCII.append(ord(element))
    print(SortedASCII)

