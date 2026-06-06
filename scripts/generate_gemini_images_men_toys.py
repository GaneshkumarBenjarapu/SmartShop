import base64
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "catalog.json"
STATIC_DIR = ROOT / "frontend" / "static"
OUTPUT_DIR = STATIC_DIR / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = os.getenv("GEMINI_IMAGE_MODEL", "gemini-2.0-flash-preview-image-generation")


def get_api_key() -> str:
    key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError(
            "Missing Gemini API key. Set GEMINI_API_KEY (or GOOGLE_API_KEY) and retry."
        )
    return key


def product_prompt(product: dict) -> str:
    name = product.get("name", "").strip()
    desc = product.get("description", "").strip()
    category = product.get("category", "").strip()
    product_id = product.get("id")

    if category == "Men Fashion":
        category_hint = (
            "men's clothing product photo, full item visible, mannequin or ghost mannequin style"
        )
    else:
        category_hint = "toy product photo, retail-packaging ready, playful but realistic"

    return (
        "Create a single realistic ecommerce hero image.\n"
        f"Product category: {category}\n"
        f"Product name: {name}\n"
        f"Product description: {desc}\n"
        f"Unique variation id: {product_id}\n"
        f"Style: {category_hint}, studio lighting, centered composition, white background.\n"
        "Requirements: no text overlays, no watermark, no logo, no collage, no humans unless needed "
        "for realistic clothing presentation, keep product highly relevant to product name."
    )


def extract_image_bytes(response_json: dict) -> bytes | None:
    candidates = response_json.get("candidates", [])
    for candidate in candidates:
        content = candidate.get("content", {})
        parts = content.get("parts", [])
        for part in parts:
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                return base64.b64decode(inline["data"])
    return None


def generate_with_gemini(prompt: str, api_key: str) -> bytes:
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{urllib.parse.quote(MODEL_NAME)}:generateContent?key={urllib.parse.quote(api_key)}"
    )
    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            raw = response.read()
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"Gemini HTTP {exc.code}: {details[:1200]}") from exc

    data = json.loads(raw.decode("utf-8"))
    image_bytes = extract_image_bytes(data)
    if not image_bytes:
        raise RuntimeError(f"No image returned by Gemini. Response: {json.dumps(data)[:600]}")
    return image_bytes


def main() -> None:
    api_key = get_api_key()
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    target = [p for p in catalog if p.get("category") in {"Men Fashion", "Toys"}]
    target.sort(key=lambda x: x.get("id", 0))

    success = 0
    failures = 0
    for product in target:
        product_id = int(product["id"])
        prompt = product_prompt(product)
        output_path = OUTPUT_DIR / f"gemini_{product_id}.png"
        try:
            image_bytes = generate_with_gemini(prompt, api_key)
            output_path.write_bytes(image_bytes)
            if output_path.stat().st_size < 1500:
                raise RuntimeError("Generated image is too small, likely invalid.")
            product["image"] = f"/static/generated/gemini_{product_id}.png"
            success += 1
            print(f"OK  {product_id} -> {product['image']}")
            time.sleep(1.0)
        except (urllib.error.URLError, RuntimeError, ValueError) as exc:
            failures += 1
            print(f"ERR {product_id}: {exc}")

    CATALOG_PATH.write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Done. success={success}, failures={failures}, total={len(target)}")


if __name__ == "__main__":
    main()
