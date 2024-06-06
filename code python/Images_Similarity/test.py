from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def check_caption_similarity(caption1, caption2):
    # Encode captions
    embeddings = model.encode([caption1, caption2], convert_to_tensor=True)

    # Calculate cosine similarity
    cosine_scores = util.pytorch_cos_sim(embeddings[0], embeddings[1])

    # Print captions and similarity score
    print("Caption 1:", caption1)
    print("Caption 2:", caption2)
    print("Cosine Similarity Score:", cosine_scores.item())

# Thay đổi các caption của bạn ở đây
caption1 = "A person is playing guitar."
caption2 = "Someone is strumming a guitar."

check_caption_similarity(caption1, caption2)