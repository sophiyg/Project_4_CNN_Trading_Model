## ResNet-18 Setup — Enaika

Loaded pretrained ResNet-18 and replaced its final layer with a
two-class output for stock direction: 0 = down/same, 1 = up.

The script preprocesses a sample candlestick chart and passes it
through the model. No training is performed, so the output scores
are only a setup check.

### How to run

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install torch torchvision pillow
python resnet_setup.py
```

The first run downloads the pretrained model weights. The sample
chart is included in `sample_images/`.

### Verification

Successfully ran `sample_images/CHAMBLFERT_002667.png` through the model:

- Input shape: [1, 3, 224, 224]
- Output shape: [1, 2]

### Dataset issue

Checked 226,068 candlestick images in my local download:
216,972 passed validation and 9,096 failed. Invalid images need
to be handled before training.

The full dataset and local Python environment are excluded from Git.

Sample image source: FinVision-21 by Dragonite_234 on Kaggle,
licensed under CC BY-NC 4.0. The sample image is unchanged.