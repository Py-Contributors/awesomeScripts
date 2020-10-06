from PIL import Image, ImageDraw
from random import randint as rint


# Definig custom function
def random_gradient(canvas):
    # specifying the image dimesion in pixels (1:1 ratio)
    dimension = 2000

    # creating a new image canvas with defined dimension
    img = Image.new("RGB", (dimension, dimension), "#000000")
    draw = ImageDraw.Draw(img)

    # generating random integers for Red, Green & Blue
    r, g, b = rint(0, 255), rint(0, 255), rint(0, 255)
    dr = (rint(0, 255) - r) / dimension
    dg = (rint(0, 255) - g) / dimension
    db = (rint(0, 255) - b) / dimension

    # filling colors in image using generated random integers
    for i in range(dimension):
        r, g, b = r + dr, g + dg, b + db
        draw.line((i, 0, i, dimension), fill=(int(r), int(g), int(b)))
    # saving canvas as .png
    img.save("gradient-" + canvas + ".png", "PNG")


# Main function
if __name__ == "__main__":
    # defining how many gradient images we want to generate i.e 30 here
    for canvas in range(30):
        # function call and creating the random canvas with gradients
        random_gradient(str(canvas))
        print("Creating Gradient Version", canvas + 1)
