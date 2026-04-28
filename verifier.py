from transformers import pipeline

nli_model = pipeline("text-classification",model="facebook/bart-large-mnli")

def verify_claim(claim, evidence):

    result = nli_model(
        evidence,
        hypothesis=claim
    )

    label = result[0]["label"]

    if label == "ENTAILMENT":
        return "SUPPORTED"

    elif label == "CONTRADICTION":
        return "REFUTED"

    else:
        return "NOT ENOUGH INFO"