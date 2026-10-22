x, y, n=map(int, input().split())
S=(x*100+y)*n
R=S//100
K=S%100
print(R,"руб.",K, "коп.")