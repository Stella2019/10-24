def sortColors(self, nums):
  red = 0
  white = 0
  blue = 0
  for num in nums:
    if num == 0:
      red += 1
    elif num == 1:
      white += 1
    else:
      blue += 1
    nums[:red] = [0] * red
    nums[red:red + white] = [1] * white
    nums[red + white:] = [2] * blue
    return nums



def sortColors(self, nums):
  left, cur, right = 0, 0, len(nums) - 1
  while cur <= right:
    if nums[cur] == 0:
      nums[cur], nums[left] = nums[left], nums[cur]
      left += 1
      cur += 1
    elif nums[cur] == 1:
      cur += 1
    else:
      nums[cur], nums[right] = nums[right], nums[cur]
      right -= 1



from collections import defaultdict

class Solution(object):
  def sortColors(self, colors):
    colorsMap = defaultdict(int)
    for c in colors:
      colorsMap[c] += 1

    index = 0
    for i in range(colorsMap[0]):
      colors[index] = 0
      index += 1
    for i in range(colorsMap[1]):
      colors[index] = 1
      index += 1
    for i in range(colorsMap[2]):
      colors[index] = 2
      index += 1

  def sortColor2(self, colors):
    lowIndex = 0
    highIndex = len(colors) - 1
    currIndex = 0

    while currIndex <= highIndex:
      if colors[currIndex] == 0:
        colors[lowIndex], colors[currIndex] = colors[currIndex], colors[lowIndex]
        lowIndex += 1
        currIndex += 1
      elif colors[currIndex] == 2:
        colors[highIndex], colors[currIndex] = colors[currIndex], colors[highIndex]
        highIndex -= 1
      else:
        currIndex += 1

colors = [0, 2, 1, 0, 1, 1, 2]
Solution().sortColors(colors)
print(colors)
# [0, 0, 1, 1, 1, 2, 2]

colors = [0, 2, 1, 0, 1, 1, 2]
Solution().sortColor2(colors)
print(colors)
# [0, 0, 1, 1, 1, 2, 2]