n = input("줄의 개수를 입력해주세요.")



if not n.isdigit():

    print("정수형으로 입력해주세요.")



elif (int(n) <= 0) or (int(n) > 100):

    print("1 이상 100 이하로 입력해주세요.")

else:

    for i in range(1, int(n) + 1):

        for k in range(i):

            print("*", end = "")

        print("")
