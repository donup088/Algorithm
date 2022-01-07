N,M=map(int,input().split())
data=[]
ans=''
dis=0
for _ in range(N):
  data.append(input())
for i in range(M):
  a,c,g,t=0,0,0,0
  for j in range(N):
    if data[j][i]=='T':
      t+=1
    elif data[j][i]=='A':
      a+=1
    elif data[j][i]=='G':
      g+=1
    elif data[j][i]=='C':
      c+=1
  if max(a,c,g,t)==a:
    ans+='A'
    dis+=c+g+t
  elif max(a,c,g,t)==c:
    ans+='C'
    dis+=a+g+t
  elif max(a,c,g,t)==g:
    ans+='G'
    dis+=a+c+t
  elif max(a,c,g,t)==t:
    ans+='T'
    dis+=a+g+c
print(ans)
print(dis)