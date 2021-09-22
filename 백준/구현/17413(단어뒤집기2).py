import sys
sys.stdin=open("input.txt","r")

s=input()
reverse = True
answer = ''
word = ''
for c in s:
  if c == '<':
    reverse = False
    answer += word
    word = '<'
  elif c == '>':
    reverse = True
    answer += (word + '>')
    word = ''
  elif c == ' ':
    answer += (word + ' ')
    word = ''
  elif reverse:
    word = c + word
  else:
    word += c

print(answer + word)
