def merge_sort(list, start=0, end=None):
    if end is None:
        end = len(list)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid, end)
        merge(list, start, mid, end)

    return list


def merge(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            list[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            list[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            list[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            list[general_index] = right[right_index]
            right_index = right_index + 1

# REFERENCIA: COURSE TRYBE


def is_anagram(first_string, second_string):

    string_1 = list(first_string.lower())
    string_2 = list(second_string.lower())

    string_1_sorted = merge_sort(string_1)
    string_2_sorted = merge_sort(string_2)

    if first_string == "" or second_string == "":
        return (
            "".join(string_1_sorted),
            "".join(string_2_sorted),
            False
        )

    return (
        "".join(string_1_sorted),
        "".join(string_2_sorted),
        string_1_sorted == string_2_sorted
    )
