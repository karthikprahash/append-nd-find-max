# append-nd-find-max
y,u=map(int,input().split())
t=list(map(int,input().split()))[:y]
r=list(map(int,input().split()))[:u]
for i in r:
    t.append(i)
    print(max(t),end=' ')
