
while True:
    num = list(input("请随机输入一个五位数："))
    if len(num) == 5:
        if num[0] is "0":
            print("---没有0开头的回生数！---")
        elif len(set(num)) == 1:
            print("---没有五位相等的回生生数---")
        elif (num[0] != num[4]) or (num[1] != num[3]):
            print("---您输入的不是回生数！---")
        else:
            print("您输入的回生数为：%s" % num)
            break
    else:
        print("输入错误！\n"
              "---请输入五位随机数---")