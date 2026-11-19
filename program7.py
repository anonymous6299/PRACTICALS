'''
AIM= Implementation of Perspective Transformation. 

REL. TH.=Perspective transformation is an image processing technique used to change the viewpoint of an image. It helps convert a perspective view into a desired view by mapping four corresponding points from the source image to the destination image. OpenCV provides getPerspectiveTransform() and warpPerspective() functions to perform this operation. It is commonly used in document scanning and image correction.

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

# Define four points in the original image
src_points = np.float32([
    [50, 50],
    [width - 50, 50],
    [50, height - 50],
    [width - 50, height - 50]
])

# Define destination points
dst_points = np.float32([
    [0, 0],
    [width - 1, 0],
    [100, height - 1],
    [width - 100, height - 1]
])

# Calculate perspective transformation matrix
M = cv2.getPerspectiveTransform(
    src_points, dst_points
)

# Apply perspective transformation
transformed = cv2.warpPerspective(
    img, M, (width, height)
)

# Display original and transformed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(transformed)
plt.title("Perspective Transformed Image")
plt.axis("off")

plt.tight_layout()
plt.show()

print("Perspective transformation completed successfully.")
'''
LO=
1. Understand perspective transformation.
2. Identify corresponding points in an image.
3. Apply perspective correction using OpenCV.
'''