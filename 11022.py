case_count = input("케이스의 개수를 입력해주세요.")

if not case_count.isdigit():

    print("정수형으로 입력해주세요.")

    

elif int(case_count) < 1:

    print("1 이상으로 입력해주세요.")

    

else:

    for i in range(1, int(case_count) + 1):

        a = input("a값을 입력해주세요.")

        b = input("b값을 입력해주세요.")

        if (not a.isdigit()) or (not b.isdigit()):

            print("a와 b는 정수여야합니다.")

        else:

            print("Case #1:", a, "+", b, "=", int(a) + int(b))
