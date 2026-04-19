# from sentence_transformers import SentenceTransformer
# import faiss
# import numpy as np

# embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# with open("rag_data.txt", "r") as f:
#     docs = f.read().split("\n\n")

# embeddings = embed_model.encode(docs)

# index = faiss.IndexFlatL2(embeddings.shape[1])
# index.add(np.array(embeddings))

# def retrieve_context(query):
#     query_vec = embed_model.encode([query])
#     D, I = index.search(np.array(query_vec), k=1)
#     return docs[I[0][0]]

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load docs
with open("rag_data.txt", "r") as f:
    text = f.read()

# 🔥 Better chunking
docs = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

embeddings = embed_model.encode(docs)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def retrieve_context(query):
    query_vec = embed_model.encode([query])
    D, I = index.search(np.array(query_vec), k=2)  # top 2

    results = [docs[i] for i in I[0]]
    return " ".join(results)