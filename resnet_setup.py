import torch
from torch import nn
from torchvision.models import resnet18, ResNet18_Weights
from PIL import Image

# Load the pretrained model.
weights = ResNet18_Weights.DEFAULT
model = resnet18(weights=weights)

# Replace the final layer so it outputs two class scores.
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 2)

print("ResNet-18 loaded successfully!")
print("New final layer:", model.fc)

# Open a valid candlestick image and convert it to RGB.
image = Image.open("sample_images/CHAMBLFERT_002667.png").convert("RGB")

# Apply the preprocessing expected by the pretrained model.
preprocess = weights.transforms()
image_tensor = preprocess(image)

# Add a batch dimension to represent one image.
image_batch = image_tensor.unsqueeze(0)

# Run the model without training.
model.eval()

with torch.no_grad():
    output = model(image_batch)

print("Input shape:", image_batch.shape)
print("Output shape:", output.shape)
print("Raw scores:", output)
print("Setup check only: the final layer has not been trained.")