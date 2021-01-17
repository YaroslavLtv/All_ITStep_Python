# #Сортировка выборкой
# def selection_sort(nums):
#     # Значение i будет соответствовать колчеству отсортированных элементов
#     for i in range(len(nums)):
#         #Исходно считаем наименьшим первый элемент
#         lowest_value_index = i
#         #Этот цикл перебирает несортированные элементы
#         for j in range(i+1, len(nums)):
#             if nums[j] < nums[lowest_value_index]:
#                 lowest_value_index = j
#                 # print(nums)
#         #Самый маленький элемент меняем с первым в списке
#         c = nums[i]
#         nums[i] = nums[lowest_value_index]
#         nums[lowest_value_index] = c
#         #test
#         # print(nums)
# l = [12,3,21,45,2,13]
# selection_sort(l)
# print(l)
#
# l = [12,3,21,45,2,13]
# l.sort()
# print(l)

#Сортировка вставками
# def insertion_sort(nums):
#     #Сортировку начинаем со второго элемента, так как считается, что первый отсортированный.
#     for i in range(1,len(nums)):
#         item_to_insert = nums[i]
#         #Сохраняем ссылку на индекс предыдущего элемента
#         j = i - 1
#         #Элемент отсортированного сегмента перемещаем вперёд, если он больше элемента для вставки
#         while j >= 0 and nums[j] > item_to_insert:
#             nums[j + 1] = nums[j]
#             j = j - 1
#         #Вставка элемента
#         nums[j + 1] = item_to_insert
#         # print(nums)
#
# l = [12,3,21,45,2,13,5,7,18,34]
# insertion_sort(l)
# print(l)

#Сортировка слиянием
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = 0
    right_list_index = 0

    #Длинна списков, так как она будет часто использоваться
    left_list_legth = len(left_list)
    right_list_legth = len(right_list)
    for _ in range(left_list_legth + right_list_legth):
        if left_list_index < left_list_legth and right_list_index < right_list_legth:
            #Сравниваем первые элементы в начале каждого списка
            #Если первый элемент левого списка меньше, добавляем его в отсортированный массив
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

def merge_sort(nums): #[12,3,21,45,2,13,5,7,18,34]
    #Возвращает список, если он равен одному элементу
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid]) #[12,3,21,45,2]
    #left_list #[12,3,21
    #
    right_list = merge_sort(nums[mid:]) #[13,5,7,18,34]

    return merge(left_list,right_list)

l = [12,3,21,45,2,13,5,7,18,34]
s = merge_sort(l)
print(s)

#Пирамидальная сортировка
def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — допустимый индекс, а элемент больше,
    # чем текущий наибольший, обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент больше не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

#Быстрая сортировка
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
