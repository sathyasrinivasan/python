import myfile
print (myfile.title)
st= 'Apple'

st[1]
st[-1]
st[2:5]
len(st)
st[:]


L=[123, 'abc',54.33,{12.3,33}]

L[0]
L[1]
L[2]
L[3]

MX=[ [1,2,3],[4,5,6],[7,8,9]]
MX[0][2]

[row[1] for row in MX]


[c for c in 'spam']

G=(sum(row) for row in MX)
next(G)
next(G)
next(G)


list(map(sum,MX))


[ord(x) for x in 'sathya']
{ord(x) for x in 'sathya'}
{x: ord(x) for x in 'sathya'}

for n in 'apple butter coffee' :
    print(n)

i = 10
while i >0 :
    print (i)
    i -=1

f = open('data.txt','w')
    f.write('Hello')
    f.close()

dir(f)

help(f.seek)

rf=open('data.txt')

df = rf.read()
print(df)
