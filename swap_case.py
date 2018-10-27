'''
Program to swap case
'''
print('Enter a string')
s=input().strip()
l=len(s)
s1=[]
for i in range(l):
    if s[i].isupper():
        s1.append(s[i].lower())
    else:
        s1.append(s[i].upper())
print("After swapping case","".join(s1))
