import math


def SubarrayProduct(numbers, k):
    subsets = []
    for i in range(len(numbers)):
        subsets.append([numbers[i]])
        for j in range(i + 1, len(numbers)):
            subset = subsets[-1]
            curr_subset = subset + [numbers[j]]
            subsets.append(curr_subset)
    counter = 0
    for subset in subsets:
        if math.prod(subset) <= k:
            counter += 1
            print(subset)
    return counter


if __name__ == '__main__':
    print(SubarrayProduct([2, 3, 4], 6))
