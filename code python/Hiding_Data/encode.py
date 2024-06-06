from PIL import Image

def file_to_binary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return ''.join(format(ord(char), '016b') for char in content)

def hide_file_in_image(image_path, file_path, output_path, spacing=1):
    img = Image.open(image_path)
    binary_file = file_to_binary(file_path)
    file_length = len(binary_file)

    width, height = img.size
    max_bytes = width * height * 3 // 8

    if file_length > max_bytes - 32:  # 32 bits để lưu trữ độ dài của file
        print("File is too large to hide in the image.")
        return

    # Ẩn độ dài của file vào ảnh
    for i in range(32):
        bit = (file_length >> (31 - i)) & 1

        value = i * spacing
        x = value // (height * 3)
        y = (value % (height * 3)) // 3
        c = value % 3

        pixel = list(img.getpixel((x, y)))
        pixel[c] = pixel[c] & 0xFE | bit
        img.putpixel((x, y), tuple(pixel))

    # Ẩn nội dung của file vào ảnh
    for i in range(32, file_length + 32):
        bit = int(binary_file[i - 32])
        
        value = i * spacing
        x = value // (height * 3)
        y = (value % (height * 3)) // 3
        c = value % 3

        pixel = list(img.getpixel((x, y)))
        pixel[c] = pixel[c] & 0xFE | bit
        img.putpixel((x, y), tuple(pixel))
        
    img.save(output_path)
    print("File hidden successfully.")

# Example usage:
hide_file_in_image("parrot.jpg", "secret.txt", "hidden_image.png", spacing=5)
