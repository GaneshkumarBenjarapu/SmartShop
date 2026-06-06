import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "catalog.json"
STATIC_DIR = ROOT / "frontend" / "static"


def as_static(path: Path) -> str:
    return f"/static/{path.name}"


def main() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))

    men_products = sorted(
        [p for p in catalog if p.get("category") == "Men Fashion"],
        key=lambda x: x["id"],
    )
    toy_products = sorted(
        [p for p in catalog if p.get("category") == "Toys"],
        key=lambda x: x["id"],
    )

    men_candidates = sorted(
        [
            p
            for p in STATIC_DIR.glob("men_*")
            if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"} and p.is_file()
        ],
        key=lambda p: p.stat().st_size,
        reverse=True,
    )
    toy_candidates = sorted(
        [p for p in STATIC_DIR.glob("amazon_toy_*.jpg") if p.is_file()],
        key=lambda p: p.name,
    )

    if len(men_candidates) < len(men_products):
        raise ValueError(
            f"Not enough men images: have {len(men_candidates)}, need {len(men_products)}"
        )
    if len(toy_candidates) < len(toy_products):
        raise ValueError(
            f"Not enough toy images: have {len(toy_candidates)}, need {len(toy_products)}"
        )

    # One unique image per product.
    for product, img_path in zip(men_products, men_candidates):
        product["image"] = as_static(img_path)

    for product, img_path in zip(toy_products, toy_candidates):
        product["image"] = as_static(img_path)

    CATALOG_PATH.write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")
    print(
        f"Updated Men={len(men_products)} and Toys={len(toy_products)} "
        "with premium local images."
    )


if __name__ == "__main__":
    main()
