def selection_sort(li):
    swaps = 0
    comparisons = 0
    for i in range(0, len(li)):
        min_index = i
        for j in range(i + 1, len(li)):
            comparisons += 1
            if li[min_index] > li[j]:
                min_index = j
        if min_index != i:
            li[i], li[min_index] = li[min_index], li[i]
            swaps += 1
    print("Sorted list:", li)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)

li = [34, 21, 2, 24, 9, 73, 47, 69, 38]
selection_sort(li)
