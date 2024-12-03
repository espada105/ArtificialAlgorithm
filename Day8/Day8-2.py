def selection_sort(arr):
    print("초기 배열:", arr)
    n = len(arr)
    for i in range(n):
        min_index = i  # 현재 위치를 최솟값 인덱스로 설정
        # 정렬되지 않은 부분에서 최솟값 찾기
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:ㅅ
                min_index = j
        # 최솟값을 현재 위치로 이동
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i + 1}: {arr}")  # 각 단계 출력
    return arr

arr = [5, 3, 8, 1]
selection_sort(arr)
print("정렬된 배열:", arr)
