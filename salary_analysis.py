# xây dựng mô hình hồi quy tuyến tính đa biến sử dụng phương pháp bình phương nhỏ nhất (Least squares)
# lưu ý, ở đây không sử dụng numpy
# để phân tích mức lương (salary) của một người dựa trên các tiêu chí đi kèm trong file: salary.csv
# đây chỉ là những tính toán lý thuyết khách quan và tương đối (có thể chưa chính xác) vì:
# - còn nhiều yếu tố ảnh hưởng đến mức lương
# - mô hình có thể chưa phù hợp (còn nhiều mô hình khác)
# - thiếu sót ngay từ khâu thống kê
import pandas
import matrix

# đọc dữ liệu từ file salary.csv
dataset = pandas.read_csv("salary.csv")

# thông qua phân tích sơ bộ dữ liệu, ta có thể thấy:
# -number(mã số): không ảnh hưởng đến salary(lương)
# => ta sẽ bỏ qua number
# dạng mô hình hồi quy tuyến tính sẽ có dạng như sau:
# salary = a + b.experience + c.age + d.score

# chuyển dữ liệu gốc thành các vector
Y = dataset.iloc[:, 4].values  # salary
X1 = dataset.iloc[:, 1].values  # experience
X2 = dataset.iloc[:, 2].values  # age
X3 = dataset.iloc[:, 3].values  # score

# xử lý dữ liệu đầu vào thành dạng ma trận
# chuyển vector Y sang dạng ma trận y(1, n)
def matrix_y(Y):
    y = matrix.matrix1(Y.__len__(), 1)
    for i in range(y.__len__()):
        y[i][0] = Y[i]
    return y

# chuyển các vector X1, X2, X3 thành ma trận A
def matrix_A(X1, X2, X3):
    m = X1.__len__()  # Có bao nhiêu bộ dữ liệu
    n = 3  # có bao nhiêu biến X
    A = matrix.matrix1(m, n + 1)
    for i in range(m):
        A[i][1] = X1[i]
        A[i][2] = X2[i]
        A[i][3] = X3[i]
    return A

y = matrix_y(Y)
A = matrix_A(X1, X2, X3)

kq = matrix.anal(A, y)
print(kq)

print("mô hình hồi quy tuyến tính đa biến tìm được là:")
print("salary = {} + {}.experience + {}.age + {}.score".format(kq[0], kq[1], kq[2], kq[3]))




