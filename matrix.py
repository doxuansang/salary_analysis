# Khởi tạo ma tran 0 (ma tran vuong với tất cả phần tử có giá trị bằng 0)
def matrix0(n):
    kq = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        kq.append(row)
    return kq

# Khởi tạo ma trận chính tắc I(n)
def matrixI(n):
    kq = matrix0(n)
    for i in range(n):
        kq[i][i] = 1
    return kq

# Khởi tạo một ma trận có m dòng, n cột với tất cả phần tử có giá trị bằng 1
def matrix1(m, n): # m là số dòng, n là số cột
    kq = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(1)
        kq.append(row)
    return kq

# xử lý dữ liệu đầu vào thành dạng ma trận
# chuyển vector Y sang dạng ma trận y(1, n)
def matrix_y(Y):
    y = matrix1(Y.__len__(), 1)
    for i in range(y.__len__()):
        y[i][0] = Y[i]
    return y

# chuyển các vector X1, X2, X3 thành ma trận A
def matrix_A(X1, X2, X3):
    m = X1.__len__()  # Có bao nhiêu bộ dữ liệu
    n = 3  # có bao nhiêu biến X
    A = matrix1(m, n + 1)
    for i in range(m):
        A[i][1] = X1[i]
        A[i][2] = X2[i]
        A[i][3] = X3[i]
    return A

# Tính ma trận chuyển vị AT
def transpose(A):
    AT = []
    for i in range(A[0].__len__()):
        row = []
        for j in range(A.__len__()):
            row.append(A[j][i])
        AT.append(row)
    return AT

# Đổi vị trí hai dòng x, y trong ma trận A
def row_switch(A, x, y):
    row = A[x]
    A[x] = A[y]
    A[y] = row
# Nhân một dòng của ma trận với một số thực
def row_mul(row, k):
    row_2 = []
    for i in range(row.__len__()):
        row_2.append(row[i]*k)
    return row_2
# Trừ hai vector x = x - y
def row_sub(x, y):
    for i in range(x.__len__()):
        x[i] = x[i] - y[i]

# sử dụng gause để thực hiện phép nghịch đảo ma trận
def gauss(A):
    B = matrixI(A.__len__())  #B = A^(-1)
    n = A.__len__()
    # biến đổi A thành ma trận bậc thang
    for i in range(n - 1):
        k = A[i][i]  # đường chéo của vector
        x = i + 1  # dòng ngay bên dưới dòng i
        # kiểm tra đường chéo, nếu có 1 vị trí trong đường chéo bằng 0
        # => ma trận không khả nghịch
        while k == 0:
            row_switch(A, i, x)
            row_switch(B, i, x)
            k = A[i][i]
            x = x + 1
            if x == n:
                return 0
        A[i] = row_mul(A[i], 1 / k)
        B[i] = row_mul(B[i], 1 / k)
        for j in range(i + 1, n):
            x = A[j][i]
            row_sub(A[j], row_mul(A[i], x))
            row_sub(B[j], row_mul(B[i], x))
    if A[n-1][n-1] != 0:
        x = 1 / (A[n - 1][n - 1])
        A[n - 1] = row_mul(A[n - 1], x)
        B[n - 1] = row_mul(B[n - 1], x)
    # hoàn tất biến đổi sang dạng bậc thang
    # tiếp tục biến đổi ma trận A thành dạng chính tắc
    for i in range(n-1):
        for j in range(i+1, n):
            x = A[i][j]
            row_sub(A[i], row_mul(A[j], x))
            row_sub(B[i], row_mul(B[j], x))
    # hoàn thành biến đổi, A trở thành ma trận chính tắc
    # ta thu được B là ma trận nghịch đảo của A
    return B

# nhân hai ma trận A, B
def matrix_mul(A, B):
    kq = []
    n = A.__len__()
    for i in range(n):
        row = []
        for j in range(B[0].__len__()):
            row.append(0)
            for k in range(n):
                row[j] = row[j] + A[i][k]*B[k][j]
        kq.append(row)
    return kq

# Sử dụng phương pháp bình phương nhỏ nhất (Least squares)
# Tính kq = (AT.A)^(-1).AT.y
# kq = [a, b, c, d]
# salary = a + b.experience + c.age + d.score
def anal(A, y):
    kq = matrix_mul(transpose(A), A)  # kq = AT.A
    kq = gauss(kq)  # kq = (AT.A)^(-1)
    kq = matrix_mul(kq, transpose(A))  # kq = (AT.A)^(-1).AT
    kq = matrix_mul(kq, y)  # kq = (AT.A)^(-1).AT.y
    return kq
