from transformers import AutoImageProcessor, AutoModel
from PIL import Image
import requests
import torch
import torch.nn.functional as F

processor = AutoImageProcessor.from_pretrained('facebook/dinov2-base')
modelImg = AutoModel.from_pretrained('facebook/dinov2-base')

# Hàm tải và xử lý hình ảnh
def process_image(image_path):
    image = Image.open(requests.get(image_path, stream=True).raw)
    # image = Image.open(image_path)
    inputs = processor(images=image, return_tensors="pt")
    outputs = modelImg(**inputs)
    last_hidden_state = outputs.last_hidden_state
    # Trích xuất vector đặc trưng từ hidden state
    pooled_output = last_hidden_state.mean(dim=1)

    return pooled_output

def images_similarity(url1, url2):
    features1 = process_image(url1)
    features2 = process_image(url2)

    cosine_similarity = F.cosine_similarity(features1, features2)

    return cosine_similarity.item()

# print(images_similarity("face1_c.jpg", "face1_cc.jpg"))