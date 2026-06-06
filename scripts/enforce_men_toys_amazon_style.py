import json
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "catalog.json"


MEN_NAMES = [
    "Symbol Men's Regular Fit Polo T-Shirt",
    "Levi's Men's 511 Slim Fit Jeans",
    "Allen Solly Men's Solid Slim Fit Casual Shirt",
    "Peter England Men's Regular Fit Formal Trousers",
    "Roadster Men's Cotton Crew Neck T-Shirt",
    "U.S. Polo Assn. Men's Chino Trousers",
    "Van Heusen Men's Slim Fit Formal Shirt",
    "Wrangler Men's Mid-Rise Regular Fit Jeans",
    "Puma Men's Essential Logo T-Shirt",
    "Louis Philippe Men's Cotton Chino Pants",
    "Arrow Men's Slim Fit Casual Trousers",
    "Tommy Hilfiger Men's Solid Polo T-Shirt",
    "Jack & Jones Men's Relaxed Fit Cargo Trousers",
    "Pepe Jeans Men's Tapered Fit Denim Jeans",
    "Wrogn Men's Typography Printed T-Shirt",
    "The Indian Garage Co Men's Checked Casual Shirt",
    "Mast & Harbour Men's Solid Round Neck T-Shirt",
    "HIGHLANDER Men's Slim Fit Chino Trousers",
    "Campus Sutra Men's Straight Fit Jeans",
    "Raymond Men's Single Breasted Blazer",
    "WildHorn Men's Genuine Leather Office Briefcase",
]

TOY_NAMES = [
    "UNO Family Card Game",
    "LEGO Classic Large Creative Brick Box",
    "Jenga Classic Game",
    "Hasbro Connect 4 Game",
    "Operation Classic Board Game",
    "Hasbro Guess Who? Game",
    "Trouble Board Game",
    "Play-Doh Modeling Compound 10-Pack Case",
    "Rubik's Cube 3x3 Puzzle Game",
    "Battleship Classic Board Game",
    "Twister Ultimate Game",
    "NERF N-Strike Elite Disruptor Blaster",
    "Hot Wheels 9-Car Gift Pack",
    "Cards Against Humanity",
    "CATAN Board Game (Base Game)",
]


def pollinations_url(category_label: str, name: str, seed: int) -> str:
    prompt = (
        f"Professional studio photography of {category_label}: {name}, "
        "white background, high resolution, product shot"
    )
    return (
        "https://image.pollinations.ai/prompt/"
        f"{quote(prompt)}?width=800&height=1000&nologo=true&seed={seed}"
    )


def main() -> None:
    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))

    men_products = sorted(
        [p for p in data if p.get("category") == "Men Fashion"], key=lambda p: p["id"]
    )
    toy_products = sorted(
        [p for p in data if p.get("category") == "Toys"], key=lambda p: p["id"]
    )

    if len(men_products) != len(MEN_NAMES):
        raise ValueError(
            f"Men Fashion count mismatch: found {len(men_products)}, expected {len(MEN_NAMES)}"
        )
    if len(toy_products) != len(TOY_NAMES):
        raise ValueError(
            f"Toys count mismatch: found {len(toy_products)}, expected {len(TOY_NAMES)}"
        )

    for product, name in zip(men_products, MEN_NAMES):
        product["name"] = name
        product["image"] = pollinations_url("Men fashion", name, product["id"] * 37 + 101)

    for product, name in zip(toy_products, TOY_NAMES):
        product["name"] = name
        product["image"] = pollinations_url("Toy", name, product["id"] * 41 + 211)

    CATALOG_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(
        f"Updated catalog at {CATALOG_PATH} | Men: {len(men_products)} | Toys: {len(toy_products)}"
    )


if __name__ == "__main__":
    main()
