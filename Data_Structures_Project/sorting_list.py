# sorting_algorithms.py

class SortingAlgorithms:

    @staticmethod
    def merge_sort(data, key=lambda x: x):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            SortingAlgorithms.merge_sort(left_half, key=key)
            SortingAlgorithms.merge_sort(right_half, key=key)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if key(left_half[i]) < key(right_half[j]):
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1

    @staticmethod
    def bubble_sort(data, key=lambda x: x):
        n = len(data)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if key(data[j]) > key(data[j+1]):
                    data[j], data[j+1] = data[j+1], data[j]
                    swapped = True
            if not swapped:
                break

    @staticmethod
    def insertion_sort(data, key=lambda x: x):
        for i in range(1, len(data)):
            key_item = data[i]
            j = i - 1
            while j >= 0 and key(key_item) < key(data[j]):
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key_item

    @staticmethod
    def selection_sort(data, key=lambda x: x):
        n = len(data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if key(data[j]) < key(data[min_index]):
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
