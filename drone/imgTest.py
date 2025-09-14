import cv2
import numpy as np

# Load or capture image
img = cv2.imread("wiltingPlant.webp")
img = cv2.resize(img, (640, 480))

# Extract channels
b, g, r = cv2.split(img)
b = b.astype("float")
g = g.astype("float")
r = r.astype("float")

# Compute VARI
vari = (g - r) / (g + r - b + 1e-5)
vari = np.clip(vari, 0, 1)

print(vari)

# Normalize and show
vari_img = (vari * 255).astype("uint8")
cv2.imshow("VARI Vegetation Index", vari_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
