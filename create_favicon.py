from PIL import Image, ImageDraw

# Create a 32x32 image with a white background
img = Image.new('RGB', (32, 32), color='white')
draw = ImageDraw.Draw(img)

# Draw a simple 'N' in blue
draw.line([(8, 8), (8, 24)], fill='blue', width=2)
draw.line([(8, 8), (24, 24)], fill='blue', width=2)
draw.line([(24, 8), (24, 24)], fill='blue', width=2)

# Save as favicon.ico
img.save('static/favicon.ico', format='ICO') 