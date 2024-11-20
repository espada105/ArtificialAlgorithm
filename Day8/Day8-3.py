def insertion_sort(arr):
    # 첫 번째 요소는 이미 정렬된 상태로 간주, 두 번째 요소부터 시작
    for i in range(1, len(arr)):
        key = arr[i]  # 현재 정렬할 요소
        j = i - 1  # 현재 요소의 바로 이전 인덱스

        # 정렬된 부분에서 key보다 큰 값을 오른쪽으로 이동
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # 값을 한 칸 오른쪽으로 이동
            j -= 1  # 인덱스를 왼쪽으로 이동

        # key를 적절한 위치에 삽입
        arr[j + 1] = key
        # 현재 배열 상태를 출력
        print(f"{i}번째 출력 {arr}")

# 테스트 데이터
arr = [7,2,5,3,8,1]

print(f"---- 원시 배열 ----\n{arr}\n------------------ \n")
# 삽입 정렬 실행
insertion_sort(arr)
# 최종 정렬 결과 출력
print(f"최종 출력 :{arr}")
