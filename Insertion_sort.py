def insertion_sort(li):
    swaps = 0
    comparisons = 0
    for i in range(0, len(li)):
        j = i
        while j>0:
            comparisons += 1
            if li[j-1]>li[j]:
                
                li[j], li[j-1] = li[j-1], li[j]
                j=j-1
                swaps += 1
            else:
                break
    print("Sorted list:", li)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)

li = [34, 21, 2, 24, 9, 73, 47, 69, 38]
insertion_sort(li)
