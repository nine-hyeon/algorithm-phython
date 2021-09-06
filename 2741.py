n = input("100,000 이하의 자연수를 입력해주세요.")

if not n.isdigit():

    print("자연수를 입력해주세요.")

elif int(n) > 100000:

    print("n은 100,000이하여야 합니다.")

else:

    for i in range(1, int(n) + 1):

        print(i)

