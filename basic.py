import cv2
import matplotlib.pyplot as plt


def read_img_in_RGB(path, name):
    img = cv2.imread(path + name)
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_RGB


def save_img_in_RGB(img, path, name):
    cv2.imwrite(path + name, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))


def show_img(img):
    plt.imshow(img)
    plt.show()


def resize_proportionally(img, new_width):
    h, w, c = img.shape
    new_height = int(h / w * new_width)
    new_dimensions = (new_width, new_height)
    resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_AREA)
    return resized_img


# increases G channel on 12%
def increase_intensity_of_g_by(img, k):
    g_intense_img = img.copy()
    for row in g_intense_img:
        for col in row:
            new_g = int(col[1] * (1 + k))
            if new_g > 255:
                col[1] = 255
            else:
                col[1] = new_g
    return g_intense_img


def cvt_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def show_img_gray(img):
    plt.imshow(img, cmap='gray')
    plt.show()
