def longestConsecutiveSubsequence(arr):
  s = set() 

  for ele in arr: 
    s.add(ele) 
  
  ans = 0
  
  for ele in arr: 
    if (ele - 1) not in s: 
      temp = ele 
      count = 1
  
      while (temp + 1) in s: 
        temp += 1
        count += 1
  
      ans = max(ans, count) 
  
  return ans 
  
arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
print(longestConsecutiveSubsequence(arr))