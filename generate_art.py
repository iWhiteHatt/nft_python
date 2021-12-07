from PIL import Image, ImageDraw
import random

def generate_art():
    print("Generating Art!")

    # base canvas
    image_size_px = 128
    image_bg_color = (255, 255, 255)
    image = Image.new(
        "RGB", 
        size=(image_size_px, image_size_px), 
        color=image_bg_color)

    # draw lines
    draw = ImageDraw.Draw(image)
    points = []

    # generate points
    for _ in range(10):
        random_point = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px)
        )
        points.append(random_point)

    for _ in range(10):
        random_point = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px)
        )
        random_point_2 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px)
        )
        line_xy = (random_point, random_point_2)
        line_color = (0, 0, 0)
        draw.line(line_xy, fill=line_color)

    # save image
    image.save("test_image.png")


# fucking program
if __name__ == "__main__":
    generate_art()