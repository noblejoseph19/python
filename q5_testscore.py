print("Enter the 10 test scores:")
score=[]
for i in range(10):
    val=int(input())
    score.append(val)
largest=max(score)
smallest=min(score)
sum=0.0
for i in score:
    sum+=i
avg=sum/10
score.sort()

print("largest and smallest values are:",largest,",",smallest)
print("The Average of the score:",avg)
print("Second largest number is:",score[-2])
lar_vals=[]
for i in score:
    if i > 100:
        lar_vals.append(i)
if lar_vals:
    print("values greater than 100 entered:",lar_vals)
for i in range(2):
    del score[i]
sum=0.0
for i in score:
    sum+=i
avg=sum/8
print("The Average of the score after deleting  2 lowest scores:",avg)





