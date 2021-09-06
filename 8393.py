n = input("1 이상 10,000 이하의 정수를 입력해주세요.")

if not n.isdigit():

    print("n은 정수형이어야 합니다.")



elif (int(n) < 0) or (int(n) > 10000):

    print("n은 0이상 10000이하여하 합니다.")



else:

    sum_of_n = 0

    for i in range(1, int(n) + 1):

        sum_of_n += i

    print(sum_of_n)
