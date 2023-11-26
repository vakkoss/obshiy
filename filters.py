from PIL import Image, ImageFilter
import random

def blur_image(input_path, output_path):
    original_image = Image.open(input_path)
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=10))
    blurred_image.save(output_path)

def sharpness_image(input_path, output_path):
    image = Image.open(input_path)
    width, height = image.size
    sharpness_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            offset_r = random.randint(-200, 200)
            offset_g = random.randint(-200, 200)
            offset_b = random.randint(-200, 200)
            r = max(0, min(255, r + offset_r))
            g = max(0, min(255, g + offset_g))
            b = max(0, min(255, b + offset_b))
            sharpness_image.putpixel((x, y), (r, g, b))
    sharpness_image.save(output_path)

def divide_and_rotate_image(input_path, output_path):
    original_image = Image.open(input_path)
    width, height = original_image.size
    half_width = width // 2
    left_part = original_image.crop((0, 0, half_width, height))
    right_part = original_image.crop((half_width, 0, width, height))
    rotated_right_part = right_part.rotate(180)
    result_image = Image.new("RGB", (width, height))
    result_image.paste(left_part, (0, 0))
    result_image.paste(rotated_right_part, (half_width, 0))
    result_image.save(output_path)

def darken_image(input_path, output_path, factor=0.3):
    original_image = Image.open(input_path)
    width, height = original_image.size
    pixels = original_image.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                int(r * factor),
                int(g * factor),
                int(b * factor)
            )
    original_image.save(output_path)