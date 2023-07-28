from sentence_transformers import SentenceTransformer
from app.settings import MODEL_NAME


model = SentenceTransformer(MODEL_NAME)


encode_sentences = lambda sentences: model.encode(sentences).tolist()