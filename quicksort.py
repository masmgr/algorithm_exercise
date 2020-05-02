import random


def quicksort(target_list):
    if len(target_list) > 1:
        p = target_list[len(target_list) // 2]
        smaller = [n for n in target_list if n < p]
        bigger = [n for n in target_list if n > p]

        return quicksort(smaller) + [p] + quicksort(bigger)

    return target_list


if __name__ == "__main__":
    N = 100
    sample_list = random.sample(range(0, N), N)
    print(sample_list)

    sample_list = quicksort(sample_list)

    print(sample_list)
