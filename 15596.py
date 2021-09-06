def sum_of_list(number_list):

    a = number_list.split(" ")

    result = 0

    for i in a:

        result += int(i)

    return result



str = input("더할 숫자들을 입력해주세요.(숫자는 공백으로 구분합니다.)")

print(sum_of_list(str))
