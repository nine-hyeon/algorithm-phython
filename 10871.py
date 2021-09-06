n_x = input("N과 X를 차례로 입력해주세요.")

arr = n_x.split(" ")

if len(arr) != 2:

    print("N과 X의 값을 모두 입력해주세요,")



else:

    type = True

    for i in arr:

        if not i.isdigit():

            print("N 혹은 X는 정수형이어야 합니다.")

            type = False

            break

    if type:

        question = arr[0] + "개의 숫자를 순서대로 입력해주세요.(공백으로 숫자 구분)"

        number_list = input(question)

        for i in number_list.split(" "):

            if int(i) < int(arr[1]):

                print(i, end = " ")
