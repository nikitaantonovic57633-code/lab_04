def bubble_sort(lst):
    if type(lst) != list:
        raise TypeError
    for n in lst:
        if type(n) != int:
            raise TypeError
    ans = lst.copy()
    for i in range(1, len(lst)):
        count = 0
        for j in range(len(lst) - i):
            if ans[j] > ans[j + 1]:
                ans[j], ans[j + 1] = ans[j + 1], ans[j]
                count += 1
        if count == 0:
            break
    return ans