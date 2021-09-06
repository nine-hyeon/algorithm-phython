base_number = input("아무 숫자나 입력해주세요.")

if not base_number.isdigit():

    print("정수형으로 입해주세요.")

else:

    for i in range(1, 10):

        print(base_number, "X", i, "=", i * int(base_number))
