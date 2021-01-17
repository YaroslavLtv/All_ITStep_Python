def binary_search(user_list, searched_element, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if searched_element == user_list[mid]:
        return mid
    if searched_element < user_list[mid]:
        return binary_search(user_list, searched_element, start, mid-1)
    else:
        return binary_search(user_list, searched_element, mid+1, end)


def linear_search(user_num, user_list):
    for i in range(len(user_list)):
        if user_list[i] == user_num:
            return i


def bubble_sort(user_list):
    while True:
        a = 1
        flag = True
        while True:
            if user_list[-a] < user_list[-(a + 1)]:
                c = user_list[-a]
                user_list[-a] = user_list[-(a + 1)]
                user_list[-(a + 1)] = c
                flag = False
            a = a + 1
            if a >= len(user_list):
                break
        if flag:
            break


def selection_sort(user_list):
    for i in range(len(user_list)):
        lowest_value_index = i
        for j in range(i+1, len(user_list)):
            if user_list[j] < user_list[lowest_value_index]:
                lowest_value_index = j
        c = user_list[i]
        user_list[i] = user_list[lowest_value_index]
        user_list[lowest_value_index] = c


def insertion_sort(user_list):
    for i in range(1, len(user_list)):
        item_to_insert = user_list[i]
        j = i - 1
        while j >= 0 and user_list[j] > item_to_insert:
            user_list[j + 1] = user_list[j]
            j = j - 1
        user_list[j + 1] = item_to_insert


def heapify(user_list, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and user_list[left_child] > user_list[largest]:
        largest = left_child
    if right_child < heap_size and user_list[right_child] > user_list[largest]:
        largest = right_child
    if largest != root_index:
        user_list[root_index], user_list[largest] = user_list[largest], user_list[root_index]
        heapify(user_list, heap_size, largest)


def heap_sort(user_list):
    n = len(user_list)
    for i in range(n, -1, -1):
        heapify(user_list, n, i)
    for i in range(n - 1, 0, -1):
        user_list[i], user_list[0] = user_list[0], user_list[i]
        heapify(user_list, i, 0)


# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
         # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        left_side = arr[:mid]

        # into 2 halves
        right_side = arr[mid:]

        # Sorting the first half
        merge_sort(left_side)

        # Sorting the second half
        merge_sort(right_side)

        i = 0
        j = 0
        k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1


# Швидке сортування
def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)