import matplotlib.pyplot as plt
import numpy as np


def show_gray_histogram(gray_img):
    y, x, _ = plt.hist(gray_img.ravel(), bins=256)
    plt.xlabel('Интенсивность $n$')
    plt.ylabel('Количество $h(n)$')
    plt.show()


def show_RGB_histogram(RGB_img):
    y, x, _ = plt.hist(RGB_img[:, :, 0].ravel(), bins=256, color='Red', alpha=0.5, density=True)
    y, x, _ = plt.hist(RGB_img[:, :, 1].ravel(), bins=256, color='Green', alpha=0.5, density=True)
    y, x, _ = plt.hist(RGB_img[:, :, 2].ravel(), bins=256, color='Blue', alpha=0.5, density=True)
    plt.hist(RGB_img.ravel(), bins=256, color='orange', alpha=0.5, density=True)

    plt.legend(['Красный канал (R)', 'Зеленый канал (G)', 'Cиний канал (B)', 'Сумма по каналам'])
    plt.xlabel('Интенсивность $n$')
    plt.ylabel('Частота')
    plt.show()


def normalize_RGB(RGB_img):
    RGB_img_new = RGB_img.copy()
    RGB_img_new[:, :, 2] = (RGB_img_new[:, :, 2] - np.min(RGB_img_new[:, :, 2])) / (
                np.max(RGB_img_new[:, :, 2]) - np.min(RGB_img_new[:, :, 2])) * 255
    RGB_img_new[:, :, 0] = (RGB_img_new[:, :, 0] - np.min(RGB_img_new[:, :, 0])) / (
                np.max(RGB_img_new[:, :, 0]) - np.min(RGB_img_new[:, :, 0])) * 255
    RGB_img_new[:, :, 1] = (RGB_img_new[:, :, 1] - np.min(RGB_img_new[:, :, 1])) / (
                np.max(RGB_img_new[:, :, 1]) - np.min(RGB_img_new[:, :, 1])) * 255
    return RGB_img_new
