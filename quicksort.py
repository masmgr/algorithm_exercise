import random

def med3(x, y, z):
    if x < y:
        if y < z:
            return y
        elif z < x:
            return x
        else:
            return z
    else:
        if z < y:
            return y
        elif x < z:
            return x
        else:
            return z


def quicksort(target_list):
    return quicksort_sub(target_list, 0, len(target_list) - 1)


def quicksort_sub(target_list, index_left, index_right):
    if index_left < index_right:
        i = index_left
        j = index_right

        p = med3(target_list[i], target_list[i + ((j - i) // 2)], target_list[j])

        while True:
            while target_list[i] < p:
                i += 1
            while target_list[j] > p:
                j -= 1
            
            if i >= j:
                break
            
            target_list[i], target_list[j] = target_list[j], target_list[i]
            i += 1
            j -= 1

        target_list = quicksort_sub(target_list, index_left, i - 1)
        target_list = quicksort_sub(target_list, j + 1, index_right)

    return target_list


if __name__ == "__main__":
    N = 100
    sample_list = random.sample(range(0, N), N)
    print(sample_list)

    sample_list = quicksort(sample_list)

    print(sample_list)
