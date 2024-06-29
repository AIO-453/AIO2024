num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
num_list[:3]
result = []
max = 1e-5

for i in range(len(num_list)-k+1): # sliding window -k+1 phần quá biên
    for j in range(k):               # duyệt từng phần tử trong sliding window
        if max < num_list[i:i+k][j]:   # so sánh max với phần tử trong sliding window
            max = num_list[i:i+k][j]     # chọn giá trị lớn nhất
    result.append(max)

print(result)

