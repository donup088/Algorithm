s=input()
result=['']*len(s)

def dfs(arr,start):
  if len(arr)==0:
    return 
  m=min(arr)
  idx=arr.index(m)
  result[start+idx]=m
  print(''.join(result))
  dfs(arr[idx+1:],start+idx+1)
  dfs(arr[:idx],start)

dfs(s,0)