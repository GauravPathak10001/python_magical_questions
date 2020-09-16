#programe to input a number upto 5 digits.
number = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
ten=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Sevemteen","Eighteen","Nineteen"]
nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
n = int(input("enter the number"))
d = [0,0,0,0,0]
num = ""
while n > 0:
    for i in ranged:
        d[i]=(n%10)
        n = n//10
print(d)
if d[4] != 0:
    if d[4] == 1:
        num += ten[d[3]]+"thousand"
    else:
        num += nty[d[4]]+number[d[3]]+"thousand"

if d[2] != 0:
    num += number[d[2]]+"Hundred"

if d[1] != 0 :
    if d[1] == 1:
        num += ten[d[0]]
    else:
        num += nty[d[1]]+number[d[0]]

print(num)
