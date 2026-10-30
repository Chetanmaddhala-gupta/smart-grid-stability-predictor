"""Execute the project's MLP and XGBoost training notebooks in order."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROJECT_DIR = Path(__file__).resolve().parent
NOTEBOOKS = ("train_mlp.ipynb", "train_xgboost.ipynb")


def display(value: Any) -> None:
    """Provide the small part of IPython's display API used by these notebooks."""
    to_string = getattr(value, "to_string", None)
    print(to_string() if callable(to_string) else value)


def execute_notebook(path: Path) -> None:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace = {"__name__": "__main__", "display": display}
    print(f"\n===== Training from {path.name} =====", flush=True)

    for index, cell in enumerate(notebook.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue

        source = "".join(cell.get("source", []))
        print(f"--- cell {index} ---", flush=True)
        exec(compile(source, f"{path.name}:cell-{index}", "exec"), namespace)

    print(f"===== Finished {path.name} =====", flush=True)


def main() -> None:
    for name in NOTEBOOKS:
        execute_notebook(PROJECT_DIR / name)


if __name__ == "__main__":
    main()
