import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

# Define chessboard dimensions
rows = 7
cols = 7

# Prepare object points
objp = np.zeros((rows * cols, 3), np.float32)
objp[:, :2] = np.mgrid[0:cols, 0:rows].T.reshape(-1, 2)

# Store object and image points
objpoints = []
imgpoints = []

# Read calibration images
images = glob.glob("calibration_images/*.jpg")

for image_path in images:
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find chessboard corners
    ret, corners = cv2.findChessboardCorners(
        gray, (cols, rows), None
    )

    if ret:
        objpoints.append(objp)

        # Refine corner positions
        corners2 = cv2.cornerSubPix(
            gray, corners, (11, 11), (-1, -1),
            (cv2.TERM_CRITERIA_EPS +
             cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        )

        imgpoints.append(corners2)

        # Draw detected corners
        cv2.drawChessboardCorners(
            img, (cols, rows), corners2, ret
        )

        print("Chessboard detected:", image_path)

# Check calibration images
if len(objpoints) == 0:
    print("No chessboard corners detected!")
    exit()

# Perform camera calibration
ret, camera_matrix, dist_coeffs, rvecs, tvecs = (
    cv2.calibrateCamera(
        objpoints, imgpoints, gray.shape[::-1],
        None, None
    )
)

# Display calibration results
print("\nCamera Matrix:")
print(camera_matrix)

print("\nDistortion Coefficients:")
print(dist_coeffs)

print("\nReprojection Error:")
print(ret)

# Read an image for distortion correction
img = cv2.imread(images[0])

# Get optimal camera matrix
h, w = img.shape[:2]

new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(
    camera_matrix, dist_coeffs, (w, h), 1, (w, h)
)

# Undistort the image
undistorted = cv2.undistort(
    img, camera_matrix, dist_coeffs,
    None, new_camera_matrix
)

# Display original and corrected images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(undistorted, cv2.COLOR_BGR2RGB))
plt.title("Undistorted Image")
plt.axis("off")

plt.tight_layout()
plt.show()

print("\nCamera calibration completed successfully.")
