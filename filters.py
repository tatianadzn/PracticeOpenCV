import cv2


def Gaussian_blur_remains(RGB_img):
    RGB_img_new = cv2.GaussianBlur(RGB_img, (7,7), 3)
    RGB_img_remaining = RGB_img - RGB_img_new
    return RGB_img_remaining
