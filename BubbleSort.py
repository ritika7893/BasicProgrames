def bubble_sort(li):
    swaps = 0
    comparisons = 0
    for i in range(0, len(li)-1):
        for j in range(0, len(li)-i-1):
            comparisons += 1
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                swaps += 1
    print("Sorted list:", li)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)
    print(li)
li=[34,21,2,24,9,73,4]
bubble_sort(li)
