# 수 정렬하기 2
import sys
sys.stdin = open('input.txt', 'r')

# 첫번째 radix sort
# def counting_sort(arr, digit):
#     n = len(arr)
#
#     result = [0] * n
#     count = [0] * 10
#
#     for i in range(n):
#         index = int(arr[i]/digit)
#         count[(index % 10)] += 1
#
#     for i in range(9):
#         count[i + 1] += count[i]
#
#     for i in range(n-1, -1, -1):
#         index = int(arr[i]/digit)
#         result[count[(index % 10)] - 1] = arr[i]
#         count[(index % 10)] -= 1
#
#     for i in range(n):
#         arr[i] = result[i]
#
#
# def radix_sort(arr):
#     maxNum = max(arr)
#     digit = 1
#     while int(maxNum/digit) > 0:
#         counting_sort(arr, digit)
#         digit *= 10
#
#
# N = int(input())
# arr = [int(input()) + 1000000 for _ in range(N)]
# radix_sort(arr)
# for num in arr:
#     print(num - 1000000)


# 두번째 quick sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     small_num, equal, large_num = [], [], []
#     for num in arr:
#         if num < pivot:
#             small_num.append(num)
#         elif num > pivot:
#             large_num.append(num)
#         else:
#             equal.append(num)
#     return quick_sort(small_num) + equal + quick_sort(large_num)
#
#
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# result = quick_sort(arr)
# for num in result:
#     print(num)


# 세번째 quick sort
def quick_sort(arr, start, end):
    if end <= start:
        return arr
    pivot = arr[(start + end) // 2]

    left = start
    right = end
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if start <= end:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
    quick_sort(arr, start, left - 1)
    quick_sort(arr, left, end)


N = int(input())
arr = [int(input()) for _ in range(N)]
quick_sort(arr, 0, len(arr) - 1)
for num in arr:
    print(num)

# n=int(sys.stdin.readline())
# num_list=[]
# while(n>0):#인자를 받아서 리스트에 담는다
#     n-=1
#     num_list.append(int(sys.stdin.readline()))
#
# def quick_sort(li,start,end):
#
#     if end <= start:
#         return li
#
#     pivot = li[(start + end) // 2]#가운데 값을 피벗으로
#
#     left=start
#     right=end
#     while left <= right:
#         while li[left] < pivot:
#             left += 1
#         while li[right] > pivot:
#             right -= 1
#         print(li)
#         if left <= right: #left와 right가 교차하지 않았으면
#             li[left], li[right] = li[right], li[left]
#             left, right = left + 1, right - 1
#
#
#
#     quick_sort(li,start, left - 1)
#     quick_sort(li,left, end)
#
#
# quick_sort(num_list,0,len(num_list)-1)
#
# for i in num_list:
#     print(i)







