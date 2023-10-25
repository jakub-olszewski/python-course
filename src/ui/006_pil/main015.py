from PIL import Image

# Otwieranie obrazu
img = Image.open("example.jpg")

# Wyświetlanie rozmiaru obrazu
print(img.size)

# Konwertowanie obrazu na odcienie szarości
img_gray = img.convert("L")

# Zapisywanie obrazu
img_gray.save("example_gray.jpg")
