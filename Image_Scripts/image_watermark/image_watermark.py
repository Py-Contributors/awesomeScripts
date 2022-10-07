from PIL import Image, ImageDraw, ImageFont


# Create an Image Object from an Image
input_image = Image.open("source.jpg")
width, height = input_image.size

draw = ImageDraw.Draw(input_image)
watermark_text = input("Enter your text for watermark \t")

font = ImageFont.truetype(font="./font.ttf", size=100)
textwidth, textheight = draw.textsize(watermark_text, font)

# calculate the x,y coordinates of the text
margin = 70
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), watermark_text, font=font, fill=(252, 227, 71))
input_image.show()

# Save watermarked image
input_image.save("./output_image_with_watermark.jpg")
