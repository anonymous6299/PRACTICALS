import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read two images
img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

if img1 is None or img2 is None:
    print("Error: Images not found!")
    exit()

# Convert images to RGB
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

# Initialize ORB detector
orb = cv2.ORB_create(1000)

# Detect keypoints and descriptors
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# Match features using BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Extract matched points
pts1 = np.float32([
    kp1[m.queryIdx].pt for m in matches
])

pts2 = np.float32([
    kp2[m.trainIdx].pt for m in matches
])

# Compute Fundamental Matrix
F, mask = cv2.findFundamentalMat(
    pts1, pts2, cv2.FM_RANSAC, 1.0, 0.99
)

if F is None:
    print("Fundamental Matrix could not be computed!")
    exit()

# Select inlier matches
inliers = mask.ravel() == 1

print("Fundamental Matrix:")
print(F)

print("\nTotal Matches:", len(matches))
print("Inlier Matches:", np.sum(inliers))

# Draw matching points
matched_img = cv2.drawMatches(
    img1, kp1, img2, kp2,
    matches[:30], None,
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

# Display images and matches
plt.figure(figsize=(12, 6))
plt.imshow(matched_img)
plt.title("Feature Matching Between Two Images")
plt.axis("off")
plt.show()

print("\nFundamental Matrix computed successfully.")
