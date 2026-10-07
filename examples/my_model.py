"""Minimal predictor stub. Run with:

    uv run benchmark.py --predictor examples/my_model.py:predict --split test

`image_path` is the full path to one image in data/images/. Return either
class names (["fasade", "snitt"]) or dicts with optional score and bbox:
{"label": "fasade", "score": 0.9, "bbox": [x1, y1, x2, y2]}.
"""


def predict(image_path: str) -> list:
    # Replace with your model. This dummy predicts nothing, so it scores 0%.
    return []
