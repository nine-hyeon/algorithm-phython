a = input("0 이상의 정수를 입력해주세요: ")

b = input("10 이하의 정수를 입력해주세요: ")

if (not a.isdigit()) or (not b.isdigit()) or int(a) < 0 or int(b) > 10:

    print("a 혹은 b가 조건을 만족하지 못했습니다.")

else:

    print('A + B = ', int(a) + int(b))
