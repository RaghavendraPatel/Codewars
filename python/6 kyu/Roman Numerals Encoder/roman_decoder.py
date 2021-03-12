def solution(n):
    dict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    num = 0
    for i,j in enumerate(n):
      try:
        if dict[j] < dict[n[i+1]]:
            num-=dict[j]
        else:
          num+=dict[j]
      except:
        num+=dict[j]
        break
    return num
