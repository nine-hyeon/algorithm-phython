def get_count_of_Hansoo(num):

    result = 0

    for i in range(1, num + 1):

        if len(str(i)) <= 2:

            result += 1

        else:

            n = str(i)

            if (int(n[0]) - int(n[1])) == (int(n[1]) - int(n[2])):

                result += 1

    return result



num = input("1 이상 1,000 이하인 정수를 입력해주세요.")



if not num.isdigit():

    print("정수형으로 입력해주세요.")

    

elif (int(num) < 1) or (int(num) > 1000):

    print("1 이상 1,000 이하로만 입력 가능합니다.")



else:

    count_H = get_count_of_Hansoo(int(num))

    print(num + "에 대한 한수의 개수:", count_H)

