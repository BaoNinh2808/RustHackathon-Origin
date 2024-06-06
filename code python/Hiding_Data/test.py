import numpy as np

# Kích thước của mảng 3 chiều
width = 10
height = 10
colors = 3

# Tạo mảng 3 chiều với các giá trị ngẫu nhiên
array_3d = np.random.randint(0, 10, size=(width, height, colors))

# In mảng 3 chiều
print("Mảng 3 chiều:")
print(array_3d)

# Ánh xạ giá trị 1 chiều vào 3 chiều
def map_value_to_3d(value, array_3d):
    # Tính toán vị trí của giá trị trong mảng 3 chiều
    width_idx = value // (height * colors)
    height_idx = (value % (height * colors)) // colors
    color_idx = value % colors
    return width_idx, height_idx, color_idx

for value in range(100):
    # Tìm vị trí của giá trị trong mảng 3 chiều
    width_idx, height_idx, color_idx = map_value_to_3d(value, array_3d.shape)

    # In vị trí của giá trị
    print(f"Vị trí của giá trị {value} trong mảng 3 chiều: ({width_idx}, {height_idx}, {color_idx})")
