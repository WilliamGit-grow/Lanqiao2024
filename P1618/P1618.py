"1~9 三个数 比例A:B:C"

# def each_char(x):
#     x1 = x % 10
#     x2 = x // 10 % 10
#     x3 = x // 100
#     return x1, x2, x3

def judge_replicate(x,y,z):
    list = []
    # x1, x2, x3 = each_char(x)
    # y1, y2, y3 = each_char(y)
    # z1, z2, z3 = each_char(z)
    # list.append(x1)
    # list.append(x2)
    # list.append(x3)
    # list.append(y1)
    # list.append(y2)
    # list.append(y3)
    # list.append(z1)
    # list.append(z2)
    # list.append(z3)
    string = str(x)+str(y)+str(z)
    for s in string:
        if string.count(s)>1:
            return False
    # for l in list:
    #     if l == 0 or list.count(l)>1:
    #         return False
    # print(list)
    return True

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    for i in [a,b,c]:
        if i == 0:
            print("No!!!")
            quit()
    no = True
    for num1 in range(100,766):
        num2 = num1*b/a
        if num2 != int(num2):
            continue
        num2 = int(num2)

        num3 = num1*c/a
        if num3 != int(num3) or num3>1000:
            continue
        num3 = int(num3)
        string = str(num1)+str(num2)+str(num3)
        if string.find("0")!=-1:
            continue

        if (judge_replicate(num1,num2,num3)):
            print(num1,num2,num3)
            no = False
    if no:
        print("No!!!")
