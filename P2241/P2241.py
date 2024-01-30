"有一个n×m 方格的棋盘，求其方格包含多少正方形、长方形（不包含正方形)"
# def cal_square(m,n,mini):
#     sum = 0
#     for i in range(mini):
#         sum += (m-i)*(n-i)
#     return sum

def cal_rec(m,n):
    sum_square = sum_rec = 0
    for i in range(m):
        for j in range(n):
            if i==j:
                sum_square += (m-i)*(n-j)
            else:
                sum_rec += (m-i)*(n-j)
            # print(i,j)
    # print(mini)
    return sum_square,sum_rec

if __name__ == "__main__":
    n,m = map(int,input().split())
    if n*m == 0:
        print(0,0)
        exit()
    #  = cal_square(n,m,int(min(n,m)))
    sum_square, sum_rec = cal_rec(n,m)
    print(sum_square,sum_rec)
