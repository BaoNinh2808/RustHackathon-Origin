import torch
from promptcap import PromptCap
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import tempfile

# Khởi tạo các mô hình
modelCap = PromptCap("tifa-benchmark/promptcap-coco-vqa")
modelSen = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def calculate_cosine_similarity(caption1, caption2):
    # Encode captions
    embeddings = modelSen.encode([caption1, caption2], convert_to_tensor=True)

    # Calculate cosine similarity
    cosine_scores = util.pytorch_cos_sim(embeddings[0], embeddings[1])

    # # Print captions and similarity score
    # print("Cosine Similarity Score:", cosine_scores.item())

    return cosine_scores.item()

def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert('RGB')
    return img

def save_image_temp(image):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    image.save(temp_file.name)
    return temp_file.name

def check_caption_similarity(image1_url, image2_url):
    prompt = "what does the image describe?"

    # Load images from URL
    image1 = load_image_from_url(image1_url)
    image2 = load_image_from_url(image2_url)

    # Save images to temporary files
    image1_path = save_image_temp(image1)
    image2_path = save_image_temp(image2)

    # Lấy mô tả cho ảnh thứ nhất
    caption1 = modelCap.caption(prompt, image1_path)

    # Lấy mô tả cho ảnh thứ hai
    caption2 = modelCap.caption(prompt, image2_path)

    # # In ra các mô tả
    # print("Caption 1:", caption1)
    # print("Caption 2:", caption2)

    # Tính độ tương đồng giữa hai mô tả
    return calculate_cosine_similarity(caption1, caption2)

# # Thay đổi các prompt và đường dẫn ảnh của bạn ở đây
# image1_url = "https://5sfashion.vn/storage/upload/images/ckeditor/4KG2VgKFDJWqdtg4UMRqk5CnkJVoCpe5QMd20Pf7.jpg"
# image2_url = "https://ss-images.saostar.vn/w800/pc/1655895094264/saostar-ejholfpiilu8d0n3.png"

# check_caption_similarity(image1_url, image2_url)
