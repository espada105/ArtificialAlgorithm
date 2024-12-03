def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    # (7 2 5)
    # (7)통과 (2,5)병합(이미 정렬로 merge통과)
    # 7, 2, 5 병합 => 2,5,7로 left정렬됨


    right = merge_sort(arr[mid:])
    # (1,3,4) 
    # (1)통과 (3,4)병합(이미 정렬로 merge통과)
    # 1, 3, 4 병합 => 1,3,4 로 right정렬됨
    return merge(left, right)



def merge(left, right):
    result = []

    i = j = 0

    while i < len(left) and j< len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [5,2,3,7,5,4,1]
print(merge_sort(arr))


# 1. 초기 배열: [5, 2, 3, 7, 5, 4, 1]

# 2. 분할:
# [5, 2, 3]와 [7, 5, 4, 1]
# [5], [2, 3]와 [7], [5, 4, 1]
# [2], [3]와 [5], [4], [1]

# 정렬 및 병합:
# [2]와 [3] 병합 → [2, 3]
# [5]와 [2, 3] 병합 → [2, 3, 5]
# [4]와 [1] 병합 → [1, 4]
# [5]와 [1, 4] 병합 → [1, 4, 5]
# [7]와 [1, 4, 5] 병합 → [1, 4, 5, 7]

# 최종 병합:
# [2, 3, 5]와 [1, 4, 5, 7] 병합 → [1, 2, 3, 4, 5, 5, 7]
# 최종 결과