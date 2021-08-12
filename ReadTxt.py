file = open("C:\\calendear.txt", 'r', encoding='UTF8')	#읽기모드로 열기
sen = file.read()				#문자열 읽기
abc = sen.split()				#공백을 기준으로 리스트 생성
for i in abc:					#리스트의 변수 i 에 대해
    if '요일' in i:				# c 가 있는 i
        print(i.strip(',.'))	#문장부호 빼고 프린트