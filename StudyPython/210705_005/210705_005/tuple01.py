str = "파이썬 문자열"				# 문자열 변수를 선언
print(str[0])						# 리스트 처럼 동작함 첫 번째 자리의 문자 출력
print(str[-1])						# 뒤에서 첫 번째 자리의 문자 출력
#str[-1] = '렬'						# 뒤에서 첫 번째 자리의 문자값 수정(오류). 수정불가 = 리스트가 아님
card = 'red', 4, 'python', True		# card 튜플를 선언
#card = ['red', 4, 'python', True]	# card 리스트를 선언
print(card)							# card 튜플 전체 출력
print(card[1])						# card 튜플의 첫 번째 요소 출력
#card[0] = 'blue'					# card 튜플 첫 번째 요소 걊 수정(오류)