import numpy as np

def cosine_similarity(a,b):
    return np.dot(a,b)/ (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve(query_embedding,chunk_embeddings,chunks, top_k=3):
    scores=[]

    for i, emb in enumerate(chunk_embeddings):
        score= cosine_similarity(query_embedding,emb)
        scores.append((chunks[i],score))
    
    scores=sorted(scores,key= lambda x:x[1],reverse=True)

    return scores[:top_k]

