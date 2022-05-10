import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def count(arr):
  _max=1
  for i in range(n):
    cnt=1
    for j in range(1,n):
      if arr[i][j]==arr[i][j-1]:
        cnt+=1
      else:
        cnt=1
      _max=max(_max,cnt)
    cnt=1
    for j in range(1,n):
      if arr[j][i]==arr[j-1][i]:
        cnt+=1
      else:
        cnt=1
      _max=max(_max,cnt)
  return _max

n=int(input())
board=[list(input().rstrip()) for _ in range(n)]
answer=0

for i in range(n):
  for j in range(n):
    if j+1<n:
      board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
      cnt=count(board)
      answer=max(answer,cnt)
      board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
    if i+1<n:
      board[i][j],board[i+1][j]=board[i+1][j],board[i][j]
      cnt=count(board)
      answer=max(answer,cnt)
      board[i][j],board[i+1][j]=board[i+1][j],board[i][j]

print(answer)
      