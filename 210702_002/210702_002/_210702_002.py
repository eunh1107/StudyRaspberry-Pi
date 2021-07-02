aa = [10, 20, 30, 40]
print("aa[-1]은 %d, aa[-2]는 %d"%(aa[-1], aa[-2]))

print(aa[0:2])
print(aa[2:4])
print(aa[0:])


'''
aa=[]
print(type(aa))
print(len(aa))

aa.append(1)
aa.append(100)
aa.append("apple")
aa.append(3.14)

print(aa)
print(type(aa[0]))
print(type(aa[1]))
print(type(aa[2]))
print(type(aa[3]))
'''

'''
aa=[1,2,3,4]
print(aa)
print(type(aa))
print(aa[0])
hap=0
aa[0]=int(input("1번째 숫자 : "))
aa[1]=int(input("2번째 숫자 : "))
aa[2]=int(input("3번째 숫자 : "))
aa[3]=int(input("4번째 숫자 : "))
hap=aa[0]+aa[1]+aa[2]+aa[3]
ptint("합계 ==> %d" %hap)
'''


'''
a = input("숫자를 입력하시오 : ")
print(a)
print(type(a))

a=int(a)

print(a)
print(type(a))

b=200
print("숫자 출력 : %d %d %x" %(a,b,b))
'''