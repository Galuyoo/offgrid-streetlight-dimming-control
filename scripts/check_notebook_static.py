import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NOTEBOOKS_TO_CHECK = [
    ROOT / "notebooks" / "03_reproduce_review_core_results.ipynb",
]

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "data" / "README.md",
    ROOT / "requirements.txt",
    ROOT / "LICENSE",
    ROOT / "CITATION.cff",
    ROOT / "data" / "processed" / "engineered_metadata.csv",
]

FORBIDDEN_STRINGS = [
    "/content/drive",
    "MyDrive",
    "drive.mount",
    "from google.colab import drive",
    "try:\nexcept Exception:",
]

REQUIRED_MARKERS = [
    "GROUP_COL",
    "TARGET",
    "FEATURES",
    "CFG",
    "make_split",
    "fit_predict",
    "simulate_metrics",
    "trade_master",
    "REVIEW_OUTDIR",
]


def check_required_files():
    missing = [p for p in REQUIRED_FILES if not p.exists()]
    if missing:
        raise FileNotFoundError(
            "Missing required repository files:\n" +
            "\n".join(str(p.relative_to(ROOT)) for p in missing)
        )


def check_notebook(path: Path):
    print(f"Checking {path.relative_to(ROOT)}")

    if not path.exists():
        raise FileNotFoundError(path)

    with path.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    code_cells = [
        (i, "".join(cell.get("source", [])))
        for i, cell in enumerate(nb.get("cells", []), start=1)
        if cell.get("cell_type") == "code"
    ]

    full_src = "\n".join(src for _, src in code_cells)

    for forbidden in FORBIDDEN_STRINGS:
        if forbidden in full_src:
            raise AssertionError(
                f"Forbidden string found in {path.name}: {forbidden!r}"
            )

    for marker in REQUIRED_MARKERS:
        if marker not in full_src:
            raise AssertionError(
                f"Required marker missing from {path.name}: {marker}"
            )

    for i, src in code_cells:
        try:
            compile(src, f"{path.name}:cell_{i}", "exec")
        except SyntaxError as e:
            raise SyntaxError(f"Syntax error in {path.name}, cell {i}: {e}") from e

    print(f"PASS: {path.relative_to(ROOT)}")


def main():
    check_required_files()

    for nb_path in NOTEBOOKS_TO_CHECK:
        check_notebook(nb_path)

    print("All static repository checks passed.")


if __name__ == "__main__":
    main()
