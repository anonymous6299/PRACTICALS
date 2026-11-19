'''
AIM= Implementation of Geometric Transformation. 

REL. TH.=Geometric transformations are operations used to change the position, orientation, size or shape of an image. Common transformations include translation, rotation, scaling, reflection and affine transformation. OpenCV provides functions such as getRotationMatrix2D() and warpAffine() to perform these operations. These techniques are useful in image alignment, correction and computer vision applications.

CODE=
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read input image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

height, width = img.shape[:2]

# 1. Translation
M = np.float32([[1, 0, 50],
                [0, 1, 30]])

translated = cv2.warpAffine(img, M, (width, height))

# 2. Rotation
center = (width // 2, height // 2)
M = cv2.getRotationMatrix2D(center, 45, 1)

rotated = cv2.warpAffine(img, M, (width, height))

# 3. Scaling
scaled = cv2.resize(img, None, fx=0.5, fy=0.5)

# 4. Reflection
reflected = cv2.flip(img, 1)

# 5. Affine Transformation
src_points = np.float32([
    [0, 0],
    [width - 1, 0],
    [0, height - 1]
])

dst_points = np.float32([
    [0, 50],
    [width - 1, 0],
    [50, height - 1]
])

M = cv2.getAffineTransform(src_points, dst_points)

affine = cv2.warpAffine(img, M, (width, height))

# Display all transformations
images = [
    (img, "Original Image"),
    (translated, "Translation"),
    (rotated, "Rotation"),
    (scaled, "Scaling"),
    (reflected, "Reflection"),
    (affine, "Affine Transformation")
]

plt.figure(figsize=(12, 8))

for i, (image, title) in enumerate(images):
    plt.subplot(2, 3, i + 1)
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()

print("Geometric transformations completed successfully.")
'''
LO=
1. Understand different geometric transformations.
2. Apply rotation, scaling and translation.
3. Perform affine transformations using OpenCV.
'''