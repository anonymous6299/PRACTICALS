
import cv2
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread("image.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display original image
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(2, 3, 2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")

# Resize image
resized = cv2.resize(img_rgb, (200, 200))

plt.subplot(2, 3, 3)
plt.imshow(resized)
plt.title("Resized Image")
plt.axis("off")

# Crop image
cropped = img_rgb[50:200, 50:200]

plt.subplot(2, 3, 4)
plt.imshow(cropped)
plt.title("Cropped Image")
plt.axis("off")

# Rotate image
rotated = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)

plt.subplot(2, 3, 5)
plt.imshow(rotated)
plt.title("Rotated Image")
plt.axis("off")

# Flip image horizontally
flipped = cv2.flip(img_rgb, 1)

plt.subplot(2, 3, 6)
plt.imshow(flipped)
plt.title("Flipped Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# Apply edge detection
edges = cv2.Canny(gray, 100, 200)

# Display additional processing results
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
plt.title("Gaussian Blur")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")
plt.axis("off")

plt.tight_layout()
plt.show()

print("Image processing operations completed successfully.")
