import re

def extract_claims(text):

    sentences = re.split(r'[.!?]', text)

    claims = []

    for s in sentences:
        s = s.strip()
        if len(s) > 5:
            claims.append(s)

    return claims