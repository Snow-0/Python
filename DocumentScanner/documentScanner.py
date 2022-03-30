# Followed this tutorial
# https://medium.datadriveninvestor.com/document-scanner-from-scratch-with-python-6a55c7ce1423
import numpy as np
import cv2
from skimage.filters import threshold_local
import math
from scipy import ndimage
print("Imports are Done!")


class Scanner:
    def __init__(self, img):
        self.img = img

    def scan_view(self):
        print("Scanned View")
        # read the original image and copies it
        # apply threshold to "scannify"

        image = cv2.imread(self.img)
        orig = image.copy()

        # covert our image to grayscale, apply threshold
        # to create scanned view effect

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thr = threshold_local(image, 11, offset=10, method="gaussian")
        image = (image > thr).astype("uint8") * 255

        # show the original image and the edge detected
        print(np.shape(orig), np.shape(image))

        # Saving a black and white image itself
        cv2.imwrite('Part_scan_view.png', image)
        return image

    def rotation(self):
        print("Rotation")
        # read the original image, copy it
        # roate it
        image = cv2.imread(self.img)
        orig = image.copy()

        img = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
        img_edges = cv2.Canny(image, 100, 100, apertureSize=3)
        lines = cv2.HoughLinesP(img_edges, rho=1, theta=np.pi /
                                180.0, threshold=160, minLineLength=100, maxLineGap=10)

        # calculate all the angles
        angles = []
        for [[x1, y1, x2, y2]] in lines:
            angle = math.degrees((math.atan2(y2-y1, x2-x1)))
            angles.append(angle)

        # average angles
        median_angle = np.median(angles)
        # actual rotation
        image = ndimage.rotate(image, median_angle)

        # saving an image itself
        cv2.imwrite("part_rotation.png", image)
        return image


if __name__ == "__main__":

    # declare image
    img = "/home/max/Python/DocumentScanner/image.jpeg"

    scan = Scanner(img)

    scanned_img = scan.scan_view()

    rotated_img = scan.rotation()
