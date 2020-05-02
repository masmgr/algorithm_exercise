import random

def quicksort(target_list):
    return quicksort_sub(target_list, 0, len(target_list) - 1)


def quicksort_sub(target_list, index_left, index_right):
    if index_left < index_right:
        target_index = index_left + ((index_right - index_left) // 2)

        i = index_left
        j = index_right
        while True:
            while target_list[i] < target_list[target_index]:
                i += 1
            while target_list[j] > target_list[target_index]:
                j -= 1
            
            if i >= j:
                break
            
            target_list[i], target_list[j] = target_list[j], target_list[i]
            i += 1
            j -= 1

        target_list[index_left:i - 1] = quicksort_sub(target_list, index_left, i - 1)[index_left:i - 1]
        target_list[j + 1:index_right] = quicksort_sub(target_list, j + 1, index_right)[j + 1:index_right]

    return target_list


if __name__ == "__main__":
    N = 100
    sample_list = random.sample(range(0, N), N)
    print(sample_list)

    sample_list = quicksort(sample_list)

    print(sample_list)
