#Note: The solution was corrected to use "+= 1" in order to account for repeating characters.

#There is also a small technicality in the time-complexity analysis.  In the video, I defined "n" as the number of words, and "m" as the average number of characters in each word.  Therefore, in the optimal solution, we must scan through each character of each word, so the time-complexity is O(n * m).  (In the video, I stated it to be linear time "O(n)", which is also correct in a sense if you were to redefine "n" to be the "size of the input," which would be the total number of characters in all the words).

import collections

def hashkey(str):
  return "".join(sorted(str))

def hashkey2(str):
  arr = [0] * 26
  for c in str:
    arr[ord(c) - ord('a')] += 1
  return tuple(arr)

def groupAnagramWords(strs):
  groups = collections.defaultdict(list)
  for s in strs:
    groups[hashkey2(s)].append(s)

  return tuple(groups.values())

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# (['abc', 'cba'], ['bcd', 'cbd'], ['efg'])