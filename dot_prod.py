'''
Program to find dot product of 2 vectors
'''
print('Enter length of the vectors')
n=int(input())
print('Enter vector1')
vec1=list(map(int,input().strip().split(' ')))
print('Enter vector2')
vec2=list(map(int,input().strip().split(' ')))
dot_prod=0
for i in range(n):
    dot_prod+=vec1[i]*vec2[i]
print('Dot Product: ',dot_prod)
