dict={'번호' : 10, '성명' : '고소영', '성명' : '장동건'}

print(dict)
print(type(dict))
print(dict['번호'])
print(dict['성명'])

print(dict.keys())
key=dict.keys()
print(type(key))
# print(key[0]) 지원 안 함
key=list(dict.keys())				# c#의 경우 (list)dict.keys()
print(type(key))
key=tuple(dict.keys())				# c#의 경우 (tuple)dict.keys()
print(type(key))

print(dict.values())
values=dict.values()
print(type(values))