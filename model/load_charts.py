import json
import random
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image

from collections import Counter

if len(sys.argv) > 1:
    DATA_DIR = Path(sys.argv[1])
else: 
    DATA_DIR = Path("data/stockdataset_384")

IMAGES_DIR = DATA_DIR / "images" / "candles"
LABELS_DIR = DATA_DIR / "labels"

print("Images folder exists:", IMAGES_DIR.exists())
print("Labels folder exists:", LABELS_DIR.exists())

images = sorted(IMAGES_DIR.glob("*.png"))
labels = {}
for p in LABELS_DIR.glob("*.json"):
    labels[p.stem] = p

pairs = []
missing = []
for img in images:
    if img.stem in labels:
        pairs.append((img, labels[img.stem]))
    else:
        missing.append(img.name)

print("Images found:", len(images))
print("Label files found:", len(labels))
print("Matched pairs:", len(pairs))
print("Images with no label:", len(missing))

direction_counts = Counter()
symbols = Counter()
wrong = []

SAMPLE_SIZE = 10000
sample = random.sample(pairs, SAMPLE_SIZE)
print(f"Checking a random sample of {SAMPLE_SIZE} labels...")

for i, (img, label_path) in enumerate(sample):
    if i % 2000 == 0:
        print(" checked", i)
    with open(label_path) as f:
        label = json.load(f)

    direction = label["direction"]
    direction_counts[direction] += 1
    symbol = label["symbol"]
    symbols[symbol] += 1

    expected = 1 if label["future_close"] > label["current_close"] else 0
    if direction != expected:
        wrong.append(label_path.name)


print("Direction counts:", dict(direction_counts))
print("Unique stocks:", len(symbols))
print("Labels that don't match prices:", len(wrong))
if len(wrong) >0:
    print("Examples:", wrong[:5])

fig, axes = plt.subplots(2, 4, figsize=(16, 8))
for ax in axes.flat:
    ax.axis("off")

shown = 0
broken = []
for img, label_path in random.sample(sample, 50):
    if shown == 8:
        break
    try:
        picture = Image.open(img)
        picture.load()
    except Exception:
        broken.append(img.name)
        continue

    with open(label_path) as f:
        label = json.load(f)
    ax = axes.flat[shown]
    ax.imshow(picture)
    ax.set_title(f'{label["symbol"]} | direction = {label["direction"]}', fontsize=10)
    shown += 1

print("Broken images found while picking examples:", broken)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "example_charts.png", dpi=150, bbox_inches="tight")
plt.show()