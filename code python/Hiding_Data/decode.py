from PIL import Image

def binary_to_file(binary, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for i in range(0, len(binary), 16):
            char_code = int(binary[i:i+16], 2)
            char = chr(char_code)
            file.write(char)

def extract_file_from_image(image_path, output_path, spacing=1):
    img = Image.open(image_path)
    width, height = img.size

    # Lấy độ dài của file được ẩn
    file_length = 0
    for i in range(32):
        value = i * spacing
        x = value // (height * 3)
        y = (value % (height * 3)) // 3
        c = value % 3
        
        pixel = img.getpixel((x, y))
        bit = (pixel[c] & 1) << (31 - i)
        file_length |= bit

    binary_file = ''
    for i in range(32, file_length + 32):
        value = i * spacing
        x = value // (height * 3)
        y = (value % (height * 3)) // 3
        c = value % 3
        
        pixel = img.getpixel((x, y))
        bit = pixel[c] & 1
        binary_file += str(bit)

    binary_to_file(binary_file, output_path)
    print("File extracted successfully.")

# Example usage:
extract_file_from_image("hidden_image.png", "extracted_secret.txt", spacing=5)
