# Selection sort
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
                print(nums)
        c = nums[i]
        nums[i] = nums[lowest_value_index]
        nums[lowest_value_index] = c


l = [12, 3, 21, 45, 2, 13]
# selection_sort(l)
# print(l)

# Insertion sort


def insertion_sort(user_list):
    # Починаємо сортування з другого елемента, перший приймаємо відсортованим
    for i in range(1, len(user_list)):
        item_to_insert = user_list[i]
        #  Зберігаємо посилання на індекс попереднього елемента
        j = i - 1
        while j >= 0 and user_list[j] > item_to_insert:
            user_list[j + 1] = user_list[j]
            j = j - 1
        user_list[j + 1] = item_to_insert
        print(user_list)


l = [12, 3, 21, 45, 2, 13]
insertion_sort(l)
# print(l)

# Merge sort (none)
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = 0
    right_list_index = 0
    # Длинна списков, так как она будет часто использоваться
    left_list_legth = len(left_list)
    right_list_legth = len(right_list)
    for _ in range(left_list_legth + right_list_legth):
        if left_list_index < left_list_legth and right_list_index < right_list_legth:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого списка меньше, добавляем его в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index = left_list_index + 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index = right_list_index + 1
        elif left_list_index == left_list_legth:
            sorted_list.append(right_list[right_list_index])
            right_list_index = right_list_index + 1
        elif right_list_index == right_list_legth:
            sorted_list.append(left_list[left_list_index])
            left_list_index = left_list_index + 1
    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

l = [12, 3, 21, 45, 2, 13, 5, 7, 18, 34]
s = merge_sort(l)
print(s)


