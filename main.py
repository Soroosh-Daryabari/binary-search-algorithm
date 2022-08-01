def binary_search(List, item, low, high):
    while low <= high:
        middle = (low + high) // 2
        if List[middle] == item:
            return middle

        elif List[middle] < item:
            low = middle + 1

        else:
            high = middle - 1
    return "Item not found"


myList = [1, 8, 7, 9, 44, 55, 86, 97, 174, 243, 588, 4488, 568789, 5466446]
enter = int(input("Enter a number : "))
result = binary_search(myList, enter, 0, len(myList) - 1)
print(result)
