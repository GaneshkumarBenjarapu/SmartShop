import math
import re
from collections import Counter


def _tokenize(text):
    tokens = re.findall(r"\b\w+\b", text.lower())
    return [token for token in tokens if len(token) > 1]


def _vectorize(corpus):
    docs = []
    for text in corpus:
        tokens = _tokenize(text)
        docs.append(Counter(tokens))
    return docs


def _cosine_similarity(doc_a, doc_b):
    if not doc_a or not doc_b:
        return 0.0

    common_tokens = set(doc_a) & set(doc_b)
    dot_product = sum(doc_a[token] * doc_b[token] for token in common_tokens)
    norm_a = math.sqrt(sum(value * value for value in doc_a.values()))
    norm_b = math.sqrt(sum(value * value for value in doc_b.values()))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot_product / (norm_a * norm_b)


def get_user_recommendations(user_history_ids, catalog, num_recommendations=6):
    """
    Generate product recommendations using a lightweight content similarity approach.
    """
    if not catalog:
        return []

    if not user_history_ids:
        sorted_catalog = sorted(
            catalog,
            key=lambda x: (x.get('rating', 0), x.get('popularity', False)),
            reverse=True,
        )
        return sorted_catalog[:num_recommendations]

    corpus = []
    product_mapping = {}
    for idx, product in enumerate(catalog):
        product_mapping[idx] = product
        name = product.get('name', '')
        desc = product.get('description', '')
        cat = product.get('category', '')
        text = f"{name} {desc} {cat}"
        corpus.append(text)

    if not corpus:
        return []

    docs = _vectorize(corpus)
    history_indices = [idx for idx, product in product_mapping.items() if product.get('id') in user_history_ids]

    if not history_indices:
        sorted_catalog = sorted(
            catalog,
            key=lambda x: (x.get('rating', 0), x.get('popularity', False)),
            reverse=True,
        )
        return sorted_catalog[:num_recommendations]

    recommendation_scores = []
    for target_idx, target_doc in enumerate(docs):
        if target_idx in history_indices:
            continue

        sims = [_cosine_similarity(target_doc, docs[hist_idx]) for hist_idx in history_indices]
        avg_sim = sum(sims) / len(sims) if sims else 0.0
        recommendation_scores.append((avg_sim, target_idx))

    recommendation_scores.sort(key=lambda x: x[0], reverse=True)
    recommended_products = [product_mapping[idx] for _, idx in recommendation_scores[:num_recommendations]]

    if len(recommended_products) < num_recommendations:
        already_recommended = {p['id'] for p in recommended_products}
        sorted_fallback = sorted(
            catalog,
            key=lambda x: (x.get('rating', 0), x.get('popularity', False)),
            reverse=True,
        )
        for p in sorted_fallback:
            if p['id'] not in already_recommended and p['id'] not in user_history_ids:
                recommended_products.append(p)
                already_recommended.add(p['id'])
            if len(recommended_products) >= num_recommendations:
                break

    return recommended_products
