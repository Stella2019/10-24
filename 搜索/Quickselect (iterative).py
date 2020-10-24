import heapq


def findKthLargest(arr, k):
  for i in range(0, k):
    (max_value, max_index) = (arr[0], 0)
    for j in range(0, len(arr)):
      if max_value < arr[j]:
        (max_value, max_index) = arr[j], j
    arr = arr[:max_index] + arr[max_index + 1:]
  for j in range(0, len(arr)):
    if max_value < arr[j]:
      (max_value, max_index) = arr[j], j
  return max_value


def findKthLargest2(arr, k):
  return sorted(arr)[-k]


def findKthLargest2(arr, k):
  arr = list(map(lambda x: -x, arr))
  heapq.heapify(arr)
  for i in range(0, k - 1):
    heapq.heappop(arr)
  return -arr[0]


def partition(arr, low, high):
  pivot = arr[high]
  i = low
  for j in range(low, high):
    if arr[j] <= pivot:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
  arr[i], arr[high] = arr[high], arr[i]
  return i


def quickselect(arr, k):
  k = len(arr) - k
  left = 0
  right = len(arr) - 1

  while left <= right:
    pivotIndex = partition(arr, left, right)
    if pivotIndex == k:
      return arr[pivotIndex]
    elif pivotIndex > k:
      right = pivotIndex - 1
    else:
      left = pivotIndex + 1
  return -1


print(quickselect([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))