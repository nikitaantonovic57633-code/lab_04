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


def _merge(left, right):
    l, r = 0, 0
    ans = []
    while l != len(left) and r != len(right):
        if left[l] <= right[r]:
            ans.append(left[l])
            l += 1
        else:
            ans.append(right[r])
            r += 1
    ans.extend(left[l:])
    ans.extend(right[r:])
    return ans


def _merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    ans = _merge(_merge_sort(left), _merge_sort(right))
    return ans


def merge_sort(lst):
    if type(lst) != list:
        raise TypeError
    for n in lst:
        if type(n) != int:
            raise TypeError
    copy = lst.copy()
    return _merge_sort(copy)