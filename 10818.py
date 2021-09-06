n = input("숫자의 개수를 적어주세요.")

if not n.isdigit():
    print("정수형으로 입력해주세요.")

elif int(n) <= 0:
    print("숫자는 1개 이상이어야 합니다.")

else:
    question = n + "개의 숫자를 입력해주세요.(공백으로 숫자 구분)"
    ans = input(question)
    arr = ans.split(" ")
    int_max = int(arr[0])
    int_min = int(arr[0])
    for i in arr:
        if int_max < int(i):
            int_max = int(i)
        if int_min > int(i):
            int_min = int(i)
    print("최댓값:", int_max)
    print("최솟값:", int_min)
