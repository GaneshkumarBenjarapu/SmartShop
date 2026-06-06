import glob
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "catalog.json"
STATIC_DIR = ROOT / "frontend" / "static"
GENERATED_DIR = STATIC_DIR / "generated"
GENERATED_DIR.mkdir(parents=True, exist_ok=True)


def build_prompt(category: str, name: str, description: str) -> str:
    base = f"{name}. {description}".strip()
    if category == "Men Fashion":
        return (
            "Professional ecommerce product photography of men's fashion apparel, "
            f"{base}, full product, white seamless background, detailed fabric texture, "
            "studio lighting, no text, no watermark"
        )
    return (
        "Professional ecommerce product photography of toy product, "
        f"{base}, retail packaging style, white seamless background, vibrant colors, "
        "studio lighting, no text, no watermark"
    )


def pollinations_url(prompt: str, product_id: int) -> str:
    encoded = urllib.parse.quote(prompt)
    seed = product_id * 97 + 13
    return (
        f"https://image.pollinations.ai/prompt/{encoded}"
        f"?width=800&height=1000&nologo=true&seed={seed}"
    )


def pick_local_fallback(product_id: int, category: str) -> str | None:
    candidates = []

    generated_candidate = GENERATED_DIR / f"generated_{product_id}.jpg"
    if generated_candidate.exists() and generated_candidate.stat().st_size > 1000:
        candidates.append(generated_candidate)

    if category == "Toys":
        toy = STATIC_DIR / f"toy_real_{product_id}.jpg"
        if toy.exists() and toy.stat().st_size > 1000:
            candidates.append(toy)
    elif category == "Men Fashion":
        for pattern in [
            f"men_real_{product_id}.jpg",
            f"men_real_{product_id}.jpeg",
            f"men_{product_id}_*.png",
            f"men_{product_id}_*.svg",
        ]:
            for path in glob.glob(str(STATIC_DIR / pattern)):
                p = Path(path)
                if p.exists() and p.stat().st_size > 300:
                    candidates.append(p)

    if not candidates:
        return None

    rel = candidates[0].relative_to(STATIC_DIR).as_posix()
    return f"/static/{rel}"


def download_image(url: str, target_path: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as response:
            payload = response.read()
        if len(payload) < 1200:
            return False
        target_path.write_bytes(payload)
        return True
    except Exception:
        return False


def main() -> None:
    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    updated = 0
    ai_generated = 0
    fallback_used = 0

    for product in data:
        category = product.get("category", "")
        if category not in {"Men Fashion", "Toys"}:
            continue

        product_id = int(product["id"])
        name = product.get("name", "")
        description = product.get("description", "")
        target_file = GENERATED_DIR / f"generated_{product_id}.jpg"

        prompt = build_prompt(category, name, description)
        url = pollinations_url(prompt, product_id)

        ok = download_image(url, target_file)
        if ok:
            product["image"] = f"/static/generated/generated_{product_id}.jpg"
            ai_generated += 1
        else:
            fallback = pick_local_fallback(product_id, category)
            if fallback:
                product["image"] = fallback
                fallback_used += 1
            else:
                product["image"] = (
                    "/static/placeholders/clothing.svg"
                    if category == "Men Fashion"
                    else "/static/placeholders/toys.svg"
                )

        updated += 1
        print(f"Processed {product_id} | {category} | {product['image']}")

    CATALOG_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(
        f"Done. Updated: {updated}, AI generated: {ai_generated}, fallback used: {fallback_used}"
    )


if __name__ == "__main__":
    main()
