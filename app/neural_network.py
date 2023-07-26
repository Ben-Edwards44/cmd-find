from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


model = SentenceTransformer(MODEL_NAME)


encode_sentences = lambda sentences: model.encode(sentences).tolist()