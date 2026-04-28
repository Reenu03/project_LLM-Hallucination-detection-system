from src.loader import load_documents
from src.chunker import chunk_document
from src.embeddings import create_embeddings
from src.retriever import retrieve
from src.claim_extractor import extract_claims
from src.verifier import verify_claim

documents = load_documents("data/documents.txt")

all_chunk = []

for doc in documents:
    chunks= chunk_document(doc)
    all_chunk.extend(chunks)

chunk_embeddings=create_embeddings(all_chunk)

query="who created python?"
query_embedding=create_embeddings([query])[0]

results = retrieve(query_embedding, chunk_embeddings, all_chunk)

print("\nQuery:", query)

print("\nTop Results:")

for chunk, score in results:
    print(score, "->", chunk)

answer = "Python was created by Guido van Rossum in 1991. It is widely used today."

claims = extract_claims(answer)

print("\nExtracted Claims:")
print(claims)

supported = 0
refuted = 0
unknown = 0

for claim in claims:

    query_embedding = create_embeddings([claim])[0]

    results = retrieve(query_embedding, chunk_embeddings, all_chunk)

    evidence = results[0][0]

    label = verify_claim(claim, evidence)

    print("\nClaim:", claim)
    print("Evidence:", evidence)
    print("Verdict:", label)

    if label == "SUPPORTED":
        supported += 1

    elif label == "REFUTED":
        refuted += 1

    else:
        unknown += 1


total_claims = len(claims)

hallucination_score = (refuted + unknown) / total_claims * 100

print("\n----- FINAL REPORT -----")

print("Total Claims:", total_claims)
print("Supported:", supported)
print("Refuted:", refuted)
print("Not Enough Info:", unknown)

print("Hallucination Score:", hallucination_score, "%")