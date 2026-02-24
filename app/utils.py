from PIL import Image, ImageOps
import torch
from app.model import processor, model


def resize_keep_aspect(image, target_height=384):
    width, height = image.size
    new_width = int((target_height / height) * width)
    return image.resize((new_width, target_height))


def predict_text(image_file):
    # Open image
    image = Image.open(image_file).convert("RGB")

    # Improve contrast
    image = ImageOps.autocontrast(image)

    # Preserve aspect ratio resize
    image = resize_keep_aspect(image, target_height=384)

    # Convert to tensor
    pixel_values = processor(images=image, return_tensors="pt").pixel_values

    # Generate prediction (better decoding settings)
    generated_ids = model.generate(
        pixel_values,
        max_length=128,
        num_beams=5,
        early_stopping=True
    )

    text = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    return text.strip()